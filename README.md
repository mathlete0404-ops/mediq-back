# Back

## Overview

<table>

  <!-- 홈 / Home -->
  <tr>
    <th align="center">홈</th>
    <th align="center">Home</th>
  </tr>
  <tr>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/c1712567-17b7-41ee-b3e1-76e53c6df62e"
        alt="Korean Home"
        width="520"
      />
    </td>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/ae8eb9b4-4f24-4a97-bf5d-adbe816462e4"
        alt="English Home"
        width="520"
      />
    </td>
  </tr>

  <!-- 소개 / Introduction -->
  <tr>
    <th align="center">소개</th>
    <th align="center">Introduction</th>
  </tr>
  <tr>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/aee521aa-c18b-47eb-8eae-1e3348372dba"
        alt="Korean Introduction"
        width="520"
      />
    </td>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/d1d7b610-cbe8-47a6-b6c4-4a5a00ec2497"
        alt="English Introduction"
        width="520"
      />
    </td>
  </tr>
  <tr>
    <th align="center">새 채팅</th>
    <th align="center">New Chat</th>
  </tr>
  <tr>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/f6a21ef9-cf76-43a1-a412-91b20542d1f2"
        alt="Korean screenshot"
        width="520"
      />
    </td>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/08cc621e-6ba9-462b-ad9c-6fc33cd787b9"
        alt="English screenshot"
        width="520"
      />
    </td>
  </tr>
    <tr>
    <th align="center">AI 분석</th>
    <th align="center">AI Analysis</th>
  </tr>
  <tr>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/6bac52a6-1af7-495e-9627-eeb8ef756926"
        alt="Korean"
        width="520"
      />
    </td>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/1b71d8d6-5e88-4441-a8c9-d1c2e558ba30"
        alt="English"
        width="520"
      />
    </td>
  </tr>
    <tr>
    <th align="center">병원 추천 (대학)</th>
    <th align="center">Hospital Recommendation (University)</th>
  </tr>
  <tr>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/aa7a0663-54d7-4fe6-ac3b-999fabe024dc"
        alt="Korean"
        width="520"
      />
    </td>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/8771a00e-7d95-49a4-b0d2-d0b017a15f34"
        alt="English"
        width="520"
      />
    </td>
  </tr>
      <tr>
    <th align="center">병원 추천 (로컬)</th>
    <th align="center">Hospital Recommendation (Local)</th>
  </tr>
  <tr>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/7b02ce53-fefd-4481-86d9-2c8cd7a399ac"
        alt="Korean"
        width="520"
      />
    </td>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/bc96e037-69b0-41f3-9bac-77fda8e9ca3e"
        alt="English"
        width="520"
      />
    </td>
  </tr>
    </tr>
      <tr>
    <th align="center">맵</th>
    <th align="center">Map</th>
  </tr>
  <tr>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/4d444907-6054-4d74-a5d1-5ea1f1da4bc9"
        alt="Korean"
        width="520"
      />
    </td>
    <td align="center">
      <img
        src="https://github.com/user-attachments/assets/450f6925-6b42-4d48-adfa-45c77d7e4e15"
        alt="English"
        width="520"
      />
    </td>
  </tr>
</table>


## Tech Stack
<img width="345" height="105" alt="Image" src="https://github.com/user-attachments/assets/1127b4eb-d3ae-4e05-af93-5a2678afa68d" />

## Project Introduction
MedIQ는 사용자가 입력한 증상 정보를 바탕으로 가장 적합한 진료과를 추천하고, 현재 위치 기준으로 신뢰도 높은 병원과 이동 경로를 안내하는 AI 기반 의료 네비게이션 웹 서비스입니다. 일상 속에서 갑작스러운 통증이나 불편함을 느꼈을 때, 많은 사람들은 “이 증상은 어느 과로 가야 하지?”, “근처에 믿을 수 있는 병원이 있을까?”, “응급 상황인지 아닌지 판단이 어렵다”와 같은 고민을 하게 됩니다. 특히 의료 지식이 부족한 일반 사용자나 외국인, 유학생의 경우 이러한 문제는 더욱 크게 다가옵니다. MedIQ는 이러한 현실적인 불편함에서 출발하여, 의료 접근성을 높이고 사용자의 의사결정을 돕는 것을 목표로 설계되었습니다.

본 서비스는 AI를 활용해 사용자가 자유롭게 입력한 증상 또는 구조화된 증상 템플릿을 분석하고, 이를 기반으로 적절한 진료과를 도출합니다. 이후 사용자의 위치 정보를 활용하여 대학병원, 유명 병원, 인근 병·의원 등을 구분하여 추천하며, Kakao Map API를 연동해 실제 지도에서 병원의 위치와 이동 경로를 직관적으로 확인할 수 있도록 구성하였습니다. 또한 병원별 전문 분야, 거리, 선택 여부 등을 고려한 인터페이스를 제공하여 사용자가 여러 병원을 비교·선택할 수 있도록 지원합니다. 단순한 검색 결과 나열이 아닌, 상황에 맞는 의료 선택을 단계적으로 안내하는 것이 MedIQ의 핵심 가치입니다.

MedIQ는 사용자 경험을 중요하게 고려하여 한국어와 영어를 모두 지원하는 다국어 환경, 라이트/다크 테마 전환, 반응형 UI 등 현대적인 웹 서비스 요소를 적극적으로 반영하였습니다. 프론트엔드에서는 React 기반 컴포넌트 구조를 활용하여 가독성과 확장성을 높였으며, 백엔드에서는 외부 지도 및 위치 API와 연동하여 실시간 데이터를 처리합니다. 본 프로젝트는 단순한 기능 구현을 넘어, 실제 사용자가 의료 서비스를 더 쉽고 빠르게 이용할 수 있도록 돕는 실용적인 문제 해결형 프로젝트로서의 의미를 갖습니다.

## Project Duration
본 프로젝트 MedIQ는 **2024년 10월부터 2025년 1월까지** 약 4개월간 진행되었습니다.  
아이디어 기획 단계부터 UI/UX 설계, 프론트엔드·백엔드 개발, AI 연동, 지도 API 통합까지 전 과정을 단독으로 수행하였습니다.  
단기간 내에 실제 사용 가능한 의료 네비게이션 서비스를 구현하는 것을 목표로 하여, 기능 구현뿐만 아니라 사용자 경험과 실사용 시나리오를 중심으로 지속적인 개선과 리팩토링을 진행하였습니다.

---

## Getting Started

MedIQ는 **증상 입력 → AI 분석 → 전문과 추천 → 병원 리스트 제공 → 지도에서 병원 위치 확인**의 흐름으로 동작하는 의료 내비게이션 웹 애플리케이션입니다.
사용자는 간단한 증상만 입력하면 AI가 이를 분석하여 적절한 진료과를 추천하고, 현재 위치를 기준으로 가까운 병원과 해당 분야에서 유명한 병원을 함께 확인할 수 있습니다.

---

## Environment Variables

MedIQ는 보안을 위해 모든 API Key를 환경 변수로 관리합니다.

### Frontend (Optional)

`mediq-front/.env.local` 파일을 생성한 뒤 아래와 같이 설정하세요.

```env
KAKAO_REST_API_KEY=YOUR_KAKAO_REST_API_KEY
NEXT_PUBLIC_BACKEND_URL=http://127.0.0.1:8000
```

* `KAKAO_REST_API_KEY`
  Kakao Local REST API 호출에 사용됩니다. 병원 검색 및 좌표 변환에 필수입니다.
* `NEXT_PUBLIC_BACKEND_URL`
  (선택 사항) Groq 기반 FastAPI 백엔드를 사용하는 경우 프론트엔드에서 호출할 주소입니다.

> ⚠️ API Key는 절대 코드에 직접 작성하지 말고 `.env.local` 파일에만 저장하세요.

---

## Kakao API Setup

MedIQ에서 병원 검색과 지도 기능을 사용하기 위해 **Kakao Developers 설정**이 필요합니다.

### Step 1) Create Kakao Application

Kakao Developers 사이트에서 로그인 후 **내 애플리케이션 → 애플리케이션 추가하기**를 통해 새 앱을 생성합니다.

### Step 2) Get REST API Key

생성된 앱의 **앱 키** 메뉴에서 **REST API 키**를 복사합니다.

### Step 3) Register Web Platform

앱 설정 → **플랫폼** 메뉴에서 **Web**을 추가하고 아래 주소를 등록합니다.

* 개발 환경: `http://localhost:3000`
* 배포 환경: 실제 서비스 도메인

이 설정이 없으면 Kakao API 호출 시 오류가 발생할 수 있습니다.

### Step 4) APIs Used in MedIQ

MedIQ에서는 아래 Kakao API 기능을 사용합니다.

* 키워드 기반 병원 검색
* 병원 주소/이름 기반 좌표 변환(Geocoding)
* 사용자 위치 기반 거리 계산

---

## Run Frontend

프론트엔드는 Next.js 기반으로 동작합니다.

```bash
cd mediq-front
npm install
npm run dev
```

실행 후 브라우저에서 아래 주소로 접속합니다.

```
http://localhost:3000
```

---

## Run Backend (mediq-back)

AI 분석을 별도의 서버(Groq + FastAPI)로 분리해 사용하는 경우에만 필요합니다.

```bash
cd mediq-back
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

환경 변수 설정 (`mediq-back/.env`):

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

서버 실행:

```bash
uvicorn main:app --reload
```

---

## Project Structure

프로젝트는 아래와 같은 구조로 구성되어 있습니다.

```
mediq-front/
 ├─ src/
 │  ├─ Components/
 │  │  ├─ hospital/
 │  │  │  ├─ HospitalList.jsx
 │  │  │  ├─ HospitalCard.jsx
 │  │  │  └─ StickyBottomBar.jsx
 │  │  ├─ lib/
 │  │  │  └─ hospitalRanking/
 │  │  │     └─ getRenownedHospitals.jsx
 │  │  ├─ contexts/
 │  │  │  └─ AppContext.jsx
 │  │  └─ common/
 │  │     ├─ Sidebar.jsx
 │  │     └─ Logo.jsx
 │  ├─ pages/
 │  │  └─ api/
 │  │     └─ kakao/
 │  │        ├─ search.js
 │  │        └─ geocode.js
 │  └─ public/
 │     └─ logo.png
```

---

## Tech Stack

* **Frontend**: Next.js, React, Tailwind CSS, Framer Motion
* **State Management**: React Context API
* **Maps & Location**: Kakao Local REST API
* **AI**: base44 InvokeLLM (기본) / Groq (선택)
* **Backend (Optional)**: FastAPI, Uvicorn

---

## Recommended Extensions

### Frontend

* ESLint
* Prettier
* Tailwind CSS IntelliSense

### Backend (mediq-back)

* Python
* Pylance

### Documentation

* GitLens
* Markdown Preview Enhanced

---

## Notes

* MedIQ에서 제공하는 결과는 **의학적 진단이 아닌 참고용 정보**입니다.
* 정확한 진단과 치료를 위해서는 반드시 의료기관을 방문하시기 바랍니다.
