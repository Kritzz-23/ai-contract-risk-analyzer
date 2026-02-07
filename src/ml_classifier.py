# src/ml_classifier.py

import joblib
from pathlib import Path

class ClauseMLClassifier:
    def __init__(self):
        model_path = Path("models/clause_classifier.pkl")
        self.model = joblib.load(model_path)

    def predict(self, clauses):
        return self.model.predict(clauses)
