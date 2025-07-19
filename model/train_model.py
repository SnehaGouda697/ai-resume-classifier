import pandas as pd
import joblib
from sklearn.base import BaseEstimator, ClassifierMixin

class RuleBasedClassifier(BaseEstimator, ClassifierMixin):
    def fit(self, X, y):
        return self

    def predict(self, X):
        results = []
        for text in X:
            text = text.lower()
            if "python" in text or "machine learning" in text or "project" in text:
                results.append("shortlisted")
            else:
                results.append("reject")
        return results

# Load data
df = pd.read_csv("resume_data.csv")
X = df["text"]
y = df["label"]

# Train rule-based model
model = RuleBasedClassifier()
model.fit(X, y)

# Save model in current folder
joblib.dump(model, "resume_classifier.pkl")
print("✅ Rule-based model saved in model/resume_classifier.pkl")




