# Income_Class_Prediction
# 💰 Income Class Prediction System

## Turning Census Attributes into Meaningful Income Insights

This project explores how demographic, educational, and employment-related attributes can be leveraged to predict an individual's income category. Built using machine learning and presented through an interactive Streamlit interface, the system classifies whether a person's annual income is likely to exceed $50K based on patterns learned from census data.

Rather than focusing solely on prediction, the project emphasizes the complete machine learning workflow — from data preparation and feature engineering to model training, evaluation, and user-facing deployment.

---

## Project Highlights

- Developed an end-to-end machine learning pipeline using the Adult Census Income Dataset.
- Performed comprehensive data preprocessing and feature transformation.
- Trained and evaluated multiple classification models.
- Achieved the strongest performance using a Random Forest Classifier.
- Designed an interactive Streamlit application for real-time predictions.
- Integrated a multi-page user interface with a motivational landing screen and prediction dashboard.
- Version controlled and published through GitHub.

---

## Dataset Overview

The model is trained on the Adult Census Income Dataset, which contains demographic and socioeconomic attributes such as:

- Age
- Education Level
- Work Class
- Occupation
- Marital Status
- Relationship Status
- Weekly Working Hours
- Capital Gain
- Capital Loss
- Native Country

The target variable categorizes income into:

- **<=50K**
- **>50K**

---

## Machine Learning Workflow

### 1. Data Preparation

- Loaded and structured raw census records.
- Handled missing and inconsistent values.
- Converted categorical variables into machine-readable representations.
- Prepared features for model training and evaluation.

### 2. Model Development

The following algorithms were explored:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

After comparative evaluation, Random Forest delivered the most reliable performance and was selected as the final model.

---

## Performance Snapshot

| Model | Accuracy |
|---------|----------|
| Logistic Regression | 81.36% |
| Decision Tree | 85.69% |
| Random Forest | 86.19% |

The Random Forest model demonstrated the best balance between predictive capability and generalization.

---

## User Interface

The application consists of two interactive screens:

### Welcome Screen

A clean landing page featuring:

- Motivational messaging
- Project introduction
- Guided entry into the prediction dashboard

### Prediction Dashboard

An intuitive interface where users can:

- Enter relevant attributes
- Generate predictions instantly
- View the predicted income category

---

## Technology Stack

**Programming Language**
- Python

**Machine Learning**
- Scikit-Learn
- Pandas
- NumPy

**Visualization & Interface**
- Streamlit

**Model Persistence**
- Joblib

**Version Control**
- Git
- GitHub

---

## Project Structure

```text
Income_Class_Prediction/
│
├── data/
│   └── adult.data
│
├── app.py
├── trainmodel.py
├── requirements.txt
├── README.md
│
└── model.pkl
```

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/Harshita29Singh/Income_Class_Prediction.git
```

Move into the project directory:

```bash
cd Income_Class_Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the Streamlit application:

```bash
streamlit run app.py
```

---

## What This Project Demonstrates

This project reflects practical experience in:

- Data preprocessing
- Feature engineering
- Classification modeling
- Model evaluation
- Streamlit application development
- Git and GitHub workflows
- End-to-end machine learning deployment

---

## Developer

**Harshita Singh**

B.Tech — Computer Science & Engineering (Artificial Intelligence & Machine Learning)

Galgotias University

Passionate about building intelligent systems that transform data into actionable insights and meaningful user experiences.

---

*"Every prediction begins as data, but its value emerges when transformed into informed decisions."*
