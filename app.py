import os
import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict_department

app = FastAPI()

# Allow local frontend (Next.js) to call this API during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Symptom(BaseModel):
    symptom: str


@app.post("/analyze")
def analyze(data: Symptom):
    symptom = data.symptom
    print(f"\n{'='*60}")
    print(f"[요청 받음] 증상 분석 시작")
    print(f"입력 증상: {symptom}")
    print(f"{'='*60}\n")

    # predict department (may raise — catch and return trace)
    try:
        dept = predict_department(symptom)
        print(f"[진료과 예측 완료] 추천 진료과: {dept}")
    except Exception as e:
        tb = traceback.format_exc()
        print("Error in predict_department:\n", tb)
        raise HTTPException(status_code=500, detail={"error": f"predict_department failed: {str(e)}", "trace": tb})

    # Try to generate a short description using a Hugging Face model if available.
    # We do lazy initialization so the server can start even if model/token are missing.
    description = None
    try:
        print(f"[AI 분석 시작] LLM 모델로 증상 분석 중...")
        gen = _get_generator()
        
        if gen is None:
            print(f"[AI 분석 건너뜀] 모델이 로드되지 않았습니다. 기본 설명 사용.")
        else:
            print(f"[프롬프트 생성] AI 모델에 전달할 프롬프트 작성 중...")
            # Create a medical prompt for the Korean medical AI model
            prompt = f"""
당신은 한국어로 응답하는 의료 내비게이션 AI입니다.
당신의 역할은 사용자의 증상을 분석하여 가장 가능성이 높은 질환, 관련된 진료과, 그 이유, 그리고 응급 여부를 판단하는 것입니다.

아래 형식(JSON)으로만 답변하세요.
불필요한 문장, 설명, 코드 블록, 마크다운은 절대 포함하지 마세요.

출력 형식:
{{
  "estimated_disease": "질병명",
  "icd_10_code": "코드",
  "specialty": "{dept}",
  "reason": "이 진료과를 추천한 이유",
  "is_emergency": true 또는 false
}}

사용자 증상: "{symptom}"
    """
            print(f"\n{'─'*60}")
            print(f"[생성된 프롬프트]")
            print(prompt)
            print(f"{'─'*60}\n")
            
            print(f"[토큰 생성 시작] AI가 답변을 생성합니다 (최대 150 토큰, 약 10-30초 소요)...")
            out = gen(prompt, num_return_sequences=1, pad_token_id=gen.tokenizer.eos_token_id)
            print(f"[토큰 생성 완료] AI 답변 생성 완료!")
            
            if isinstance(out, list) and len(out) > 0 and isinstance(out[0], dict):
                generated = out[0].get("generated_text", "")
                # Extract only the answer part after "답변:"
                if "답변:" in generated:
                    description = generated.split("답변:")[-1].strip()
                else:
                    description = generated.replace(prompt, "").strip()
            elif isinstance(out, str):
                description = out
            
            if description:
                print(f"[AI 분석 완료] 설명 생성 성공 (길이: {len(description)} 글자)")
            else:
                print(f"[AI 분석 경고] 답변이 비어있습니다.")

    except Exception as e:
        # Log error and fall back to deterministic description below
        tb = traceback.format_exc()
        print(f"[AI 분석 실패] LLM 생성 중 에러 발생:\n{tb}")

    if not description:
        description = (
            f"간단 설명: '{symptom[:200]}'와 같은 증상에서 의심할 수 있는 몇 가지 원인을 요약합니다."
            " 정확한 진단을 위해 의료기관 방문을 권장합니다."
        )
        print(f"[폴백 설명 사용] AI 생성 실패로 기본 설명 사용")

    result = {"department": dept, "description": description}
    
    print(f"\n{'='*60}")
    print(f"[응답 생성 완료] JSON 응답:")
    print(f"진료과: {result['department']}")
    print(f"설명: {result['description'][:100]}..." if len(result['description']) > 100 else f"설명: {result['description']}")
    print(f"{'='*60}\n")
    
    return result


def _get_generator():
    """Lazily create and cache a Hugging Face text generation pipeline.

    Uses ChuGyouk/ko-med-gemma-2-9b-it-merge2 - a Korean medical AI model
    trained on Korean medical datasets for symptom analysis and diagnosis recommendations.

    Controlled by environment variables:
    - HUGGINGFACE_TOKEN: (optional) if provided, used as auth token.
    - MODEL_NAME: (optional) model to load; defaults to Korean medical Gemma model.
    If model load fails, returns None and the app will fall back to a deterministic
    description.
    """
    global _generator
    try:
        _generator
    except NameError:
        _generator = None

    if _generator is not None:
        return _generator

    # model_name = os.environ.get("MODEL_NAME", "ChuGyouk/ko-med-gemma-2-9b-it-merge2") GPU
    model_name = os.environ.get("MODEL_NAME", "beomi/KoAlpaca-Polyglot-5.8B")
    hf_token = os.environ.get("HUGGINGFACE_TOKEN")
    
    try:
        from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
        import torch
        
        # Check if GPU is available
        device = 0 if torch.cuda.is_available() else -1
        device_name = "GPU" if device == 0 else "CPU"
        print(f"\n{'*'*60}")
        print(f"[모델 로딩 시작] {device_name}에서 모델 다운로드 및 초기화 중...")
        print(f"모델: {model_name}")
        print(f"{'*'*60}\n")
        
        if hf_token:
            _generator = pipeline(
                "text-generation",
                model=model_name,
                tokenizer=model_name,
                device=device,
                token=hf_token,
                max_length=512,  # Maximum input + output length
                max_new_tokens=400,  # Maximum new tokens to generate
                temperature=0.3,
                do_sample=True,
                truncation=True,
            )
        else:
            _generator = pipeline(
                "text-generation",
                model=model_name,
                tokenizer=model_name,
                device=device,
                max_length=512,  # Maximum input + output length
                max_new_tokens=400,  # Maximum new tokens to generate
                temperature=0.3,
                do_sample=True,
                truncation=True,
            )
        
        print(f"\n{'*'*60}")
        print(f"[모델 로딩 완료] ✅ Korean Medical AI 모델 설치 완료!")
        print(f"모델명: {model_name}")
        print(f"디바이스: {device_name}")
        print(f"최대 토큰: 150")
        print(f"온도: 0.7")
        print(f"{'*'*60}\n")
        
        return _generator
    except Exception as e:
        print(f"\n{'!'*60}")
        print(f"[모델 로딩 실패] ❌ Korean Medical AI 모델 초기화 실패")
        print(f"모델: {model_name}")
        print(f"에러: {e}")
        print(f"폴백 모드로 동작합니다.")
        print(f"{'!'*60}\n")
        return None


@app.get("/health")
def health():
    """Return basic health + generator status for debugging."""
    gen = None
    try:
        gen = _get_generator()
    except Exception:
        gen = None
    return {"ok": True, "hf_generator_loaded": gen is not None}
