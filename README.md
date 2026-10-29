# 🩺 Disease Prediction Model

A machine learning-based disease prediction system that predicts potential diseases based on user-selected symptoms. Built using Python and Random Forest Classification, the project combines a trained machine learning model with an interactive Streamlit application to demonstrate symptom-based disease prediction.

## 📌 Project Overview

The Disease Prediction Model analyzes a set of symptoms provided by the user and predicts a possible disease using a trained machine learning model. The application presents the predicted disease, its confidence score, alternative predictions, and general information about the predicted condition.

This project demonstrates the practical application of machine learning, data preprocessing, classification algorithms, and interactive application development in healthcare-related use cases.

## ✨ Features

- **Symptom Selection:** Search and select symptoms through an interactive interface.
- **Disease Prediction:** Predict a potential disease using a trained Random Forest Classification model.
- **Confidence Score:** Display the model's confidence score for the predicted result.
- **Alternative Predictions:** Visualize other top disease predictions using a bar chart.
- **Disease Information:** Display general information and precautions for supported conditions.
- **PDF Report Generation:** Generate and download a report containing the predicted disease and confidence score.
- **Interactive UI:** Use a Streamlit-based interface for an accessible user experience.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn, Random Forest Classifier
- **Data Processing:** Pandas, NumPy
- **Data Visualization:** Plotly, Matplotlib
- **Web Application:** Streamlit
- **PDF Generation:** ReportLab
- **Development Environment:** Jupyter Notebook

## 📂 Project Structure

```text
Disease-Prediction-Model/
│
├── data/                       # Dataset files
├── model/                      # Trained model and supporting files
├── app.py                      # Streamlit application
├── predict.py                  # Disease prediction logic
├── disease_prediction.ipynb    # Model development and experimentation
├── prediction.pdf              # Sample or generated prediction report
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/tanushreelonare/Disease-Prediction-Model.git
```

### 2. Navigate to the Project Directory

```bash
cd Disease-Prediction-Model
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
pip install streamlit
```

The additional Streamlit installation is required because the application uses Streamlit, which should also be included in `requirements.txt` for a reproducible setup.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will start in your terminal and provide a local URL, typically:

```text
http://localhost:8501
```

Open the URL in your browser to interact with the application.

## 🚀 How to Use

1. Launch the application using Streamlit.
2. Search for symptoms or select them from the available symptom categories.
3. Click the **Predict** button to submit the selected symptoms.
4. View the predicted disease and its confidence score.
5. Explore the chart showing alternative predictions.
6. Review the available disease information and general precautions.
7. Download the generated PDF prediction report if required.

## 🧠 Machine Learning Approach

The project uses a Random Forest Classifier to perform disease classification based on symptom-related input features.

The general workflow includes:

1. **Data Preparation:** Load and prepare the dataset for model development.
2. **Preprocessing:** Transform symptom and disease labels into a format suitable for machine learning.
3. **Model Training:** Train a Random Forest classification model on the prepared data.
4. **Prediction:** Process user-selected symptoms and generate a disease prediction.
5. **Result Presentation:** Display the prediction, confidence score, and alternative predictions through the application.

The Jupyter Notebook contains the model development and experimentation workflow, while `predict.py` handles prediction logic used by the application.

## 🔮 Future Improvements

- Expand and improve the training dataset to support a broader range of conditions.
- Evaluate model performance using appropriate classification metrics.
- Improve model validation and generalization to unseen data.
- Add prediction history and downloadable reports with additional details.
- Enhance the user interface and deploy the application online.
- Add automated tests for preprocessing and prediction functionality.

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes only**. Predictions are based on the dataset and trained model and may be inaccurate or incomplete. The results must not be used as a medical diagnosis, treatment recommendation, or substitute for professional medical advice. Consult a qualified healthcare professional for medical concerns.

## 👩‍💻 Author

**Tanushree Lonare**

GitHub: [@tanushreelonare](https://github.com/tanushreelonare)

Project Repository: [Disease Prediction Model](https://github.com/tanushreelonare/Disease-Prediction-Model)

---

If you find this project useful, consider giving the repository a ⭐ on GitHub!
