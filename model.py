import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

DATA_PATH = "data.csv"
MODEL_PATH = "model.pkl"

def train_model():
    df = pd.read_csv(DATA_PATH)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["symptom"])
    y = df["department"]

    clf = LogisticRegression()
    clf.fit(X, y)

    joblib.dump((vectorizer, clf), MODEL_PATH)
    print("✅ Model trained and saved.")

def predict_department(symptom):
    if not os.path.exists(MODEL_PATH):
        train_model()

    vectorizer, clf = joblib.load(MODEL_PATH)
    X = vectorizer.transform([symptom])
    return clf.predict(X)[0]
