from flask import Flask, request, jsonify
from flask_cors import CORS

def get_predicted_value(symptoms):
    if "chills" in symptoms or "cough"  in symptoms:
        return "Flu"
    return "Unknown Disease"
def helper(predicted_disease):
    if predicted_disease == "Flu":
        desc = "Influenza (flu) is a viral infection that attacks the respiratory system."
        pre = [["Drink plenty of fluids", "Get plenty of rest", "Take antiviral medications if prescribed"]]
        med = ["Paracetamol", "Ibuprofen"]
        die = ["Warm soups", "Vitamin C rich foods", "Herbal tea"]
        wrkout = ["Light stretching", "Breathing exercises"]
    else:
        desc = "No information available."
        pre, med, die, wrkout = [[]], [], [], []
    
    return desc, pre, med, die, wrkout

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    symptoms = data.get("symptoms", "")
    user_symptoms = [s.strip() for s in symptoms.split(',')]
    predicted_disease = get_predicted_value(user_symptoms)
    desc, pre, med, die, wrkout = helper(predicted_disease)
    
    return jsonify({
        "predicted_disease": predicted_disease,
        "description": desc,
        "precautions": pre[0],
        "medications": med,
        "diets": die,
        "workout": wrkout
    })

if __name__ == "__main__":
    app.run(debug=True)
