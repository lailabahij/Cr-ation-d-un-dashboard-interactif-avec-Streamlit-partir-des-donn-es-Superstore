# dashboard_fixed_v2.py
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv 
import os
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 🔗 Connexion à la DB
# -----------------------------
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# -----------------------------
# 📥 Charger les données
# -----------------------------

df_orders = pd.read_sql(
    "SELECT order_id, customer_id, product_name, order_date, ship_date FROM orders",
    engine
)

products_df = pd.read_sql(
    "SELECT product_name, category, sales, marge FROM products",
    engine
)

df_regions = pd.read_sql(
    "SELECT customer_id, region_name FROM regions",
    engine
)

# -----------------------------
# تحويل التواريخ
# -----------------------------
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'], errors='coerce')
df_orders['ship_date'] = pd.to_datetime(df_orders['ship_date'], errors='coerce')

# -----------------------------
# Feature Engineering
# -----------------------------
df_orders['month_year'] = df_orders['order_date'].dt.to_period('M')
products_df['profit_ratio'] = products_df['marge'] / products_df['sales']

# -----------------------------
# Merge Optimisé
# -----------------------------
df = df_orders.merge(
    products_df[['product_name','category','sales','marge','profit_ratio']],
    on='product_name',
    how='left'
).merge(
    df_regions[['customer_id','region_name']],
    on='customer_id',
    how='left'
)

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔎 Filtres")
region_filter = st.sidebar.selectbox("Région", ["Tous"] + sorted(df['region_name'].dropna().unique()))
category_filter = st.sidebar.selectbox("Catégorie", ["Tous"] + sorted(df['category'].dropna().unique()))
period_filter = st.sidebar.selectbox("Période (Mois-Année)", ["Tous"] + sorted(df['month_year'].astype(str).unique()))

# -----------------------------
# Appliquer les filtres
# -----------------------------
df_filtered = df.copy()
if region_filter != "Tous":
    df_filtered = df_filtered[df_filtered['region_name'] == region_filter]
if category_filter != "Tous":
    df_filtered = df_filtered[df_filtered['category'] == category_filter]
if period_filter != "Tous":
    df_filtered = df_filtered[df_filtered['month_year'].astype(str) == period_filter]

# -----------------------------
# KPIs (Key Performance Indicators)
# -----------------------------
total_sales = df_filtered['sales'].sum()
total_profit = df_filtered['marge'].sum()
profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

st.title("📊 Dashboard Commercial")
col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"{total_sales:,.0f}")
col2.metric("📈 Total Profit", f"{total_profit:,.0f}")
col3.metric("📊 Profit Margin", f"{profit_margin:.2f}%")

# -----------------------------
# Graph 1: Sales par catégorie
# -----------------------------
st.subheader("📦 Sales par catégorie")
sales_cat = df_filtered.groupby("category")["sales"].sum().reset_index()
fig1, ax1 = plt.subplots()
sns.barplot(data=sales_cat, x="category", y="sales", ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# -----------------------------
# Graph 2: Sales par mois
# -----------------------------
st.subheader("📈 Sales par mois")
sales_month = df_filtered.groupby("month_year")["sales"].sum().reset_index()
sales_month['month_year_str'] = sales_month['month_year'].astype(str)
fig2, ax2 = plt.subplots()
sns.lineplot(data=sales_month, x='month_year_str', y='sales', marker='o', ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# -----------------------------
# Graph 3: Pie chart - ventes par catégorie
# -----------------------------
st.subheader("🥧 Répartition des ventes par catégorie")
fig3, ax3 = plt.subplots()
ax3.pie(sales_cat['sales'], labels=sales_cat['category'], autopct='%1.1f%%', startangle=180)
ax3.set_title("Répartition des ventes par catégorie")
st.pyplot(fig3)

# -----------------------------
# Graph 4: Top 10 produits
# -----------------------------
st.subheader("🏆 Top 10 produits")
top_products = df_filtered.groupby('product_name')['sales'].sum().nlargest(10).reset_index()
fig4, ax4 = plt.subplots()
sns.barplot(data=top_products, x='sales', y='product_name', ax=ax4)
st.pyplot(fig4)

# -----------------------------
# Graph 5: Heatmap ventes par région et catégorie
# -----------------------------
st.subheader("🌡️ Heatmap ventes par région et catégorie")
pivot_table = df_filtered.pivot_table(values='sales', index='region_name', columns='category', aggfunc='sum')
fig5, ax5 = plt.subplots(figsize=(8,5))
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap="coolwarm", ax=ax5)
st.pyplot(fig5)

# -----------------------------
# Aperçu des données
# -----------------------------
st.subheader("📄 Aperçu des données")
st.dataframe(df_filtered.head())