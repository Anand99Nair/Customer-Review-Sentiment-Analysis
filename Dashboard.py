import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("flipkart_vader_sentiment_cleaned.csv")

# Filter out Neutral sentiment
df = df[df['Sentiment'] != 'Neutral']

# Streamlit App Configuration
st.set_page_config(page_title="Flipkart Sentiment Analysis Dashboard", layout="wide")

# Custom CSS for layout control
st.markdown("""
    <style>
        body { font-family: 'Arial', sans-serif; }
        .main .block-container { padding: 2rem; max-width: 95%; }
        h1 { text-align: center; font-size: 42px; color: #333; }
        .stButton > button { background-color: #54bebe; color: white; border-radius: 8px; padding: 8px 16px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar with Multi-Select Filter
st.sidebar.header("🔍 Product Filters")

# Get unique product names
all_products = sorted(df['Product Name'].unique())

# "Select All" Checkbox
select_all = st.sidebar.checkbox("Select All Products", value=True)

# Multi-Select Box
if select_all:
    selected_products = all_products  # Select all products by default
else:
    selected_products = st.sidebar.multiselect("Select Products", all_products, default=all_products[:5])

# Apply filter to ALL visualizations
df_filtered = df[df['Product Name'].isin(selected_products)]

# Header with Logo
col1, col2 = st.columns([0.2, 0.8])
with col1:
    st.image("Customer Review.png", width=200)
with col2:
    st.markdown("<h1>📊 Flipkart Sentiment Analysis Dashboard</h1>", unsafe_allow_html=True)

st.markdown("---")

# 🔥 Most Reviewed Products (Filtered)
st.subheader("🔥 Most Reviewed Products")
most_reviewed = df_filtered['Product Name'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(15, 6))
sns.barplot(x=most_reviewed.values, y=most_reviewed.index, 
            palette=['#54bebe', '#76c8c8', '#98d1d1', '#badbdb', '#dedad2', '#e4bcad', '#df979e'], ax=ax)
ax.set_xlabel("Review Count")
ax.set_ylabel("Product Name")
ax.set_title("Most Reviewed Products")
ax.patch.set_alpha(0.5)
st.pyplot(fig)
st.markdown("---")

# 🏆 Best & Worst Rated Products (Filtered)
st.subheader("🏆 Best & Worst Rated Products")
sentiment_scores = df_filtered.groupby('Product Name')['Sentiment'].value_counts(normalize=True).unstack().fillna(0)
sentiment_scores['Positive Ratio'] = sentiment_scores.get('Positive', 0)
best_products = sentiment_scores.sort_values(by='Positive Ratio', ascending=False).head(5)
worst_products = sentiment_scores.sort_values(by='Positive Ratio', ascending=True).head(5)

col1, col2 = st.columns(2)
with col1:
    st.write("### 🌟 Top 5 Best Rated Products")
    for product in best_products.index:
        st.write(f"✔️ {product}")
with col2:
    st.write("### ❌ Top 5 Worst Rated Products")
    for product in worst_products.index:
        st.write(f"❌ {product}")

st.markdown("---")

# 📊 Sentiment Comparison of Top 5 Products (Filtered)
st.subheader("📊 Sentiment Comparison of Top 5 Products")
top_5_products = df_filtered['Product Name'].value_counts().head(5).index
sentiment_comparison = df_filtered[df_filtered['Product Name'].isin(top_5_products)].groupby(['Product Name', 'Sentiment']).size().unstack().fillna(0)

fig, ax = plt.subplots(figsize=(15, 6))
sentiment_comparison.plot(kind='bar', stacked=True, 
                          color=['#e27c7c', '#badbdb'], ax=ax)
ax.set_xlabel("Product Name")
ax.set_ylabel("Review Count")
ax.set_title("Sentiment Comparison of Top 5 Products")
ax.legend(title="Sentiment")
ax.patch.set_alpha(0.5)
st.pyplot(fig)
st.markdown("---")

# 🔍 Most Discussed Features by Sentiment (Filtered)
st.subheader("🔍 Most Discussed Features by Sentiment")
feature_keywords = ['battery', 'camera', 'display', 'performance', 'price', 'design', 'quality']
feature_sentiment = {feature: {'Positive': 0, 'Negative': 0} for feature in feature_keywords}

for _, row in df_filtered.iterrows():
    review = row['Cleaned_Review'].lower()
    sentiment = row['Sentiment']
    for feature in feature_keywords:
        if feature in review:
            feature_sentiment[feature][sentiment] += 1

feature_df = pd.DataFrame(feature_sentiment).T
feature_df = feature_df.sort_values(by='Positive', ascending=False)
fig, ax = plt.subplots(figsize=(15, 6))
sns.barplot(x=feature_df['Positive'], y=feature_df.index, 
            palette=['#e4bcad', '#df979e', '#d7658b', '#c80064'], ax=ax)
ax.set_xlabel("Positive Mentions")
ax.set_ylabel("Feature")
ax.set_title("Most Positively Discussed Features")
ax.patch.set_alpha(0.7)
st.pyplot(fig)

st.markdown("---")
st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <p style='font-size: 18px; font-weight: bold;'>Made by <a href='https://www.linkedin.com/in/anandnair' target='_blank' style='color:#6A0DAD; text-decoration: none;'>Anand Nair</a></p>
    </div>
    """, unsafe_allow_html=True)
