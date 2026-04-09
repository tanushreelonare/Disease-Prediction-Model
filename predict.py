import pickle
import numpy as np

model = pickle.load(open("model/model.pkl", "rb"))
encoder = pickle.load(open("model/encoder.pkl", "rb"))
columns = pickle.load(open("model/columns.pkl", "rb"))

def predict_disease(symptoms):
    input_data = [0] * len(columns)

    for symptom in symptoms:
        if symptom in columns:
            index = columns.index(symptom)
            input_data[index] = 1

    input_data = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)

    predicted_label = encoder.inverse_transform(prediction)[0]
    confidence = float(max(probabilities[0]))

    # Top 5 predictions
    top_indices = np.argsort(probabilities[0])[-5:][::-1]
    top_diseases = encoder.inverse_transform(top_indices)
    top_probs = probabilities[0][top_indices]

    return predicted_label, confidence, list(zip(top_diseases, top_probs))