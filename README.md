# Flipkart Sentiment Analysis

## 📌 Introduction

Understanding customer sentiment is crucial for businesses to enhance their products and services. In this project, we performed **Sentiment Analysis** on customer reviews from Flipkart using **Web Scraping, Natural Language Processing (NLP), and Machine Learning**. The results are visualized in an interactive **Streamlit Dashboard** to provide actionable insights.

---

## 📊 Project Overview

### ✅ Problem Statement
Flipkart, being one of the largest e-commerce platforms, receives thousands of customer reviews daily. However, manually analyzing these reviews to extract meaningful insights is time-consuming and inefficient.

### 🎯 Objective
- **Automate the extraction** of customer reviews from Flipkart.
- **Classify sentiments** (Positive, Negative) using NLP and Machine Learning.
- **Provide insights** through an interactive dashboard.
- **Identify trends** in customer feedback for different products.

---

## ⚙️ Approach

### **1️⃣ Web Scraping with Selenium**
- Extracted **ratings, review titles, and review comments** from Flipkart product pages.
- Implemented **scrolling & pagination handling** for maximum data collection.
- Stored data in a structured **CSV format** for analysis.

### **2️⃣ Sentiment Analysis with NLP (VADER)**
- Preprocessed text: **removed stopwords, punctuation, and tokenized words**.
- Used **VADER (Valence Aware Dictionary and sEntiment Reasoner)** to assign sentiment scores.
- Labeled reviews as **Positive or Negative** based on sentiment scores.

### **3️⃣ Machine Learning Model for Sentiment Classification**
- Converted text into **numerical features** using **TF-IDF Vectorization**.
- Trained a **Multinomial Naive Bayes** model for sentiment classification.
- Achieved **97.9% accuracy** in predicting sentiment.

### **4️⃣ Interactive Streamlit Dashboard**
- Visualized insights through **charts, sentiment distribution, and product comparisons**.
- Included **filters, reset buttons, and ranking lists** for easy exploration.

---

## 🎯 Model Performance
| Model                 | Accuracy  |
|----------------------|-----------|
| Multinomial Naive Bayes | 97.9%       |

---

## 🖥️ Dashboard Screenshots
Here are some insights from the dashboard:

### **Most Reviewed Products**
![Most Reviewed Products](most_reviewed.png)

### **Best & Worst Rated Products**
![Best & Worst Rated Products](best_worst.png)

### **Most Discussed Features by Sentiment**
![Most Discussed Feature](most_discussed_feature.png)

---

## 🚀 Key Features
- **Automated Web Scraping**: Extracts reviews from Flipkart.
- **Sentiment Classification**: Categorizes reviews as Positive or Negative.
- **Machine Learning Model**: Provides high accuracy in sentiment prediction.
- **Interactive Dashboard**:
  - Most Reviewed Products
  - Best & Worst Rated Products
  - Sentiment Comparison of Top Products
  - Most Discussed Features by Sentiment

---

## 🔧 Installation & Usage

### **1️⃣ Install Required Libraries**
```bash
pip install selenium streamlit pandas matplotlib seaborn vaderSentiment scikit-learn
```

### **2️⃣ Run the Dashboard**
```bash
streamlit run dashboard.py
```

---

## 📢 Conclusion
This project demonstrates how **data-driven insights** can help businesses understand customer feedback at scale. By leveraging **Web Scraping, NLP, and Machine Learning**, we transformed raw Flipkart reviews into meaningful sentiment insights.

---

## 📩 Contact
**Made by:** [Anand Nair](https://www.linkedin.com/in/anandnair99/)  
For any questions, feel free to reach out!

---

