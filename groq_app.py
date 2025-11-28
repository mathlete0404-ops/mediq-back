import os
import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict_department

from dotenv import load_dotenv
load_dotenv()  # .env 파일에서 환경 변수 로드

try:
    from groq import Groq
except ImportError:  # 런타임 시 안내용
    Groq = None

app = FastAPI()

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
    print("[Groq 요청 받음] 증상 분석 시작")
    print(f"입력 증상: {symptom}")
    print(f"{'='*60}\n")

    try:
        dept = predict_department(symptom)
        print(f"[진료과 예측 완료] 추천 진료과: {dept}")
    except Exception as e:
        tb = traceback.format_exc()
        print("Error in predict_department:\n", tb)
        raise HTTPException(status_code=500, detail={"error": f"predict_department failed: {str(e)}", "trace": tb})

    if not dept or str(dept).upper() == "UNKNOWN":
        msg = "해당 증상에 맞는 진료과를 찾지 못했습니다. 증상을 조금 더 자세히 적어 다시 입력해 주세요."
        print(f"[진료과 미매칭] {msg}")
        return {"department": None, "description": msg}

    description = None
    estimated_disease = None
    icd_10_code = None
    try:
        print("[Groq AI 분석 시작] Groq LLM으로 증상 분석 중...")
        client = _get_groq_client()

        if client is None:
            print("[Groq AI 분석 건너뜀] Groq 클라이언트가 초기화되지 않았습니다.")
        else:
            prompt = f"""
            당신은 한국어를 사용하는 의료 내비게이션 AI입니다.
            사용자의 증상을 바탕으로 적절한 진료과를 추천하고, 응급 여부를 평가하며, 추정 질환과 ICD-10 코드를 제안하세요.

            반드시 아래 JSON 형식의 문자열만 한국어로 출력하세요. 불필요한 설명은 쓰지 마세요.

            {{
              "specialty": "{dept}",
              "reason": "해당 진료과를 선택한 이유",
              "is_emergency": true 또는 false,
              "estimated_disease": "추정 질환명",
              "icd_10_code": "가능성이 가장 높은 ICD-10 코드"
            }}

            사용자 증상: "{symptom}"
            """

            print("[Groq 프롬프트 생성] Groq LLM에 프롬프트 전달")
            # llama-3.1-70b-versatile 모델은 더 이상 지원되지 않으므로
            # 문서에 나온 권장 최신 모델을 기본값으로 사용합니다.
            groq_model = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
            chat_completion = client.chat.completions.create(
                model=groq_model,
                messages=[
                    {"role": "system", "content": "You are a Korean medical navigation AI assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.4,
                max_tokens=300,
            )

            content = chat_completion.choices[0].message.content if chat_completion.choices else None
            if content:
                raw_text = content.strip()
                print(f"[Groq AI 원본 응답] {raw_text}")

                # 모델이 반환한 JSON 문자열을 파싱하여 세부 필드 분리
                try:
                    import json

                    # 코드 블록("```json" 등) 안에 JSON을 넣어줄 수도 있으므로 중괄호 영역만 추출 시도
                    start = raw_text.find('{')
                    end = raw_text.rfind('}')
                    json_text = raw_text[start : end + 1] if start != -1 and end != -1 else raw_text

                    parsed = json.loads(json_text)
                    description = parsed.get("reason")
                    estimated_disease = parsed.get("estimated_disease")
                    icd_10_code = parsed.get("icd_10_code")
                    print("[Groq AI 분석 완료] JSON 파싱 성공")
                except Exception as parse_err:
                    # JSON 형식이 아닐 경우 전체 텍스트를 설명으로 사용
                    description = raw_text
                    print("[Groq AI 분석 경고] JSON 파싱 실패, 전체 텍스트를 설명으로 사용", parse_err)
            else:
                print("[Groq AI 분석 경고] 빈 응답 수신")

    except Exception as e:
        tb = traceback.format_exc()
        print(f"[Groq AI 분석 실패] Groq LLM 호출 중 에러 발생:\n{tb}")

    if not description:
        description = (
            f"간단 설명: '{symptom[:200]}'와 같은 증상에서 의심할 수 있는 몇 가지 원인을 요약합니다. "
            "정확한 진단을 위해 의료기관 방문을 권장합니다."
        )
        print("[Groq 폴백 설명 사용] Groq 응답이 없어 기본 설명 사용")

    result = {
        "department": dept,
        "description": description,
        "estimated_disease": estimated_disease,
        "icd_10_code": icd_10_code,
    }

    print(f"\n{'='*60}")
    print("[Groq 응답 생성 완료] JSON 응답:")
    print(f"진료과: {result['department']}")
    if len(str(result.get("description") or "")) > 100:
        print(f"설명: {str(result['description'])[:100]}...")
    else:
        print(f"설명: {result['description']}")
    print(f"{'='*60}\n")

    return result


def _get_groq_client():
    """Groq Python 클라이언트를 lazy 초기화합니다.

    환경 변수:
    - GROQ_API_KEY: 필수. Groq 대시보드에서 발급받은 API 키.
    - GROQ_MODEL: 선택. 기본값은 'llama-3.3-70b-versatile'.
    """
    global _groq_client
    try:
        _groq_client
    except NameError:
        _groq_client = None

    if _groq_client is not None:
        return _groq_client

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("[Groq 설정 경고] GROQ_API_KEY 환경 변수가 설정되지 않았습니다.")
        return None

    if Groq is None:
        print("[Groq 설정 경고] 'groq' 패키지가 설치되지 않았습니다. 'pip install groq'로 설치하세요.")
        return None

    try:
        _groq_client = Groq(api_key=api_key)
        print("[Groq 클라이언트 초기화 완료] Groq LLM 사용 준비 완료")
        print(f"사용 모델: {os.environ.get('GROQ_MODEL', 'llama-3.3-70b-versatile')}")
        return _groq_client
    except Exception as e:
        print("[Groq 클라이언트 초기화 실패]", e)
        return None


@app.get("/health")
def health():
    client = None
    try:
        client = _get_groq_client()
    except Exception:
        client = None
    return {"ok": True, "groq_client_loaded": client is not None}
