import streamlit as st
import time
import pickle
import plotly.graph_objects as go
from predict import predict_disease
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

columns = pickle.load(open("model/columns.pkl", "rb"))

disease_info = {
    "Fungal infection": ("Skin infection caused by fungi", "Keep skin dry, use antifungal creams"),
    "Allergy": ("Immune response to allergens", "Avoid triggers, take antihistamines"),
    "GERD": ("Acid reflux disease", "Avoid spicy food, eat smaller meals"),
    "Chronic cholestasis": ("Liver bile flow issue", "Consult doctor, maintain diet"),
    "Drug Reaction": ("Adverse reaction to medication", "Stop drug, consult doctor"),
    "Peptic ulcer disease": ("Ulcers in stomach lining", "Avoid NSAIDs, eat healthy"),
    "AIDS": ("Immune system disease", "Antiretroviral therapy"),
    "Diabetes": ("High blood sugar levels", "Monitor glucose, exercise"),
    "Gastroenteritis": ("Stomach infection", "Hydration, rest"),
    "Bronchial Asthma": ("Airway inflammation", "Use inhaler, avoid triggers"),
    "Hypertension": ("High blood pressure", "Reduce salt, exercise")
}

st.set_page_config(page_title="Disease Predictor", layout="wide")

st.markdown("""
<style>
body { background-color: #f4f8fb; }
h1 { font-size: 40px !important; color: #1f4e79; }
.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}
.result-box {
    background: linear-gradient(135deg,#89f7fe,#66a6ff);
    padding: 20px;
    border-radius: 12px;
    font-size: 24px;
    text-align:center;
    color: #003366;
    font-weight: bold;
}
.info-box {
    background: #fff3cd;
    padding: 15px;
    border-radius: 10px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🩺 AI Disease Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Search or select symptoms to predict disease</p>", unsafe_allow_html=True)

def categorize(symptoms):
    categories = {
        "General": [],
        "Pain": [],
        "Skin": [],
        "Respiratory": [],
        "Digestive": [],
        "Others": []
    }
    for s in symptoms:
        if any(k in s for k in ["fever","fatigue","weakness"]):
            categories["General"].append(s)
        elif "pain" in s or "headache" in s:
            categories["Pain"].append(s)
        elif "skin" in s or "itch" in s:
            categories["Skin"].append(s)
        elif "cough" in s or "breath" in s:
            categories["Respiratory"].append(s)
        elif "stomach" in s or "vomit" in s:
            categories["Digestive"].append(s)
        else:
            categories["Others"].append(s)
    return categories

categories = categorize(columns)

st.markdown("<div class='card'>", unsafe_allow_html=True)

search = st.text_input("🔎 Search Symptoms")
filtered_columns = [s for s in columns if search.lower() in s.lower()] if search else columns

selected_symptoms = []

for category, items in categories.items():
    items = [i for i in items if i in filtered_columns]
    if items:
        selected = st.multiselect(f"{category} Symptoms", items)
        selected_symptoms.extend(selected)

st.markdown("</div>", unsafe_allow_html=True)

def create_pdf(disease, confidence):
    file_path = "prediction.pdf"
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()
    content = []
    content.append(Paragraph(f"<b>Disease:</b> {disease}", styles["Title"]))
    content.append(Paragraph(f"<b>Confidence:</b> {round(confidence*100,2)}%", styles["Heading2"]))
    doc.build(content)
    return file_path

if st.button("🔍 Predict"):
    if not selected_symptoms:
        st.warning("⚠️ Please select symptoms first")
    else:
        with st.spinner("🧠 Analyzing symptoms..."):
            time.sleep(2)

        disease, confidence, top_preds = predict_disease(selected_symptoms)

        st.markdown(
            f"<div class='result-box'>🩺 {disease}<br>Confidence: {round(confidence*100,2)}%</div>",
            unsafe_allow_html=True
        )

        diseases = [x[0] for x in top_preds]
        probs = [x[1] for x in top_preds]

        fig = go.Figure(go.Bar(
            x=probs,
            y=diseases,
            orientation='h'
        ))
        fig.update_layout(height=300, margin=dict(l=20, r=20, t=30, b=20))

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.plotly_chart(fig, use_container_width=True)

        if disease in disease_info:
            desc, precautions = disease_info[disease]
            st.markdown(f"<div class='info-box'><b>About:</b> {desc}<br><b>Precautions:</b> {precautions}</div>", unsafe_allow_html=True)

        pdf_path = create_pdf(disease, confidence)

        with open(pdf_path, "rb") as f:
            st.download_button("📄 Download Report", f, "disease_prediction.pdf")