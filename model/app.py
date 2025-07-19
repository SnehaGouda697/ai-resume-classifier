from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)

# Load the saved model
model_path = os.path.join(os.path.dirname(__file__), 'resume_classifier.pkl')
model = joblib.load(model_path)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])   
def predict():
    data = request.get_json()
    text = data.get('text', '').lower()

    # Rule-based logic
    if "python" in text or "data science" in text:
        prediction = "shortlisted"
    else:
        prediction = "reject"

    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(debug=True)





