# 💳 Credit Risk Analysis using Machine Learning

## 📌 Project Overview

This project predicts whether a customer is **creditworthy** or **high risk** based on their financial information. The goal is to help financial institutions make better loan approval decisions by analyzing customer data using machine learning classification algorithms.

---

## 🎯 Objective

To predict an individual's creditworthiness using historical financial data and compare different machine learning models to identify the best-performing classifier.

---

## 📂 Dataset

**Dataset:** Bank Loans Dataset

The dataset contains customer financial information, including:

* Age
* Education Level
* Employment Years
* Years at Current Address
* Annual Income
* Debt-to-Income Ratio
* Credit Debt
* Other Debt

**Target Variable:**

* **Default**

  * **0** = Creditworthy Customer
  * **1** = High Risk Customer (Loan Default)

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

---

## 🤖 Machine Learning Models

The following classification models were implemented and compared:

* Logistic Regression
* Decision Tree
* Random Forest

---

## 📊 Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Score
* Confusion Matrix

---

## 🏆 Best Performing Model

After comparing all models, **Logistic Regression** achieved the best overall performance.

### Performance

* **Accuracy:** 85.00%
* **Precision:** 81.48%
* **Recall:** 57.89%
* **F1-Score:** 67.69%
* **ROC-AUC:** 76.50%

---

## 🚀 Features

* Data preprocessing
* Missing value handling
* Correlation analysis
* Model training and evaluation
* Model comparison
* Credit risk prediction
* Interactive Streamlit web application

---

## 📁 Project Structure

```
Credit_Risk_Analysis/
│
├── app.py
├── credit_risk_model.pkl
├── requirements.txt
├── bankloans.csv
├── Credit_Risk_Analysis.ipynb
└── README.md
```

---

## ▶️ How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 💻 Web Application

The Streamlit application allows users to enter customer financial information and instantly predicts whether the customer is:

* ✅ Creditworthy Customer
* ⚠️ High Risk Customer (Loan Default)

---

## 📌 Conclusion

This project demonstrates the use of machine learning techniques for credit risk assessment. Among the evaluated models, Logistic Regression provided the best balance of accuracy and predictive performance, making it the most suitable model for this dataset.

---

## 👩‍💻 Author

**Adeena Waqar**
