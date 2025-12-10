python3 -m venv venv
source venv/bin/activate
pip install NAME
uvicorn app(FileName):app --reload
uvicorn groq_app:app --reload 