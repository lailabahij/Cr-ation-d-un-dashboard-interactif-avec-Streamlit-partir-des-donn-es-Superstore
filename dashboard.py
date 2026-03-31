<<<<<<< HEAD
# dashboard_fixed_v2.py
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv 
=======
# dashboard.py
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
>>>>>>> 2794616986a5b29be7eef30bfe6d328b089baccb
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
<<<<<<< HEAD

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
=======
df_orders = pd.read_sql("SELECT * FROM orders", engine)
products_df = pd.read_sql("SELECT * FROM products", engine)
df_regions = pd.read_sql("SELECT * FROM regions", engine)
df_customers = pd.read_sql("SELECT * FROM customers", engine)

df_orders['order_date'] = pd.to_datetime(df_orders['order_date'], errors='coerce')
df_orders['ship_date'] = pd.to_datetime(df_orders['ship_date'], errors='coerce')
print("Valeurs nulles dans orders_df :\n", df_orders.isnull().sum())
print("Valeurs nulles dans products_df :\n", products_df.isnull().sum())
print("Valeurs nulles dans customers_df :\n", df_customers.isnull().sum())
print("Valeurs nulles dans regions_df :\n", df_regions.isnull().sum())
# -----------------------------
# Feature engineering
>>>>>>> 2794616986a5b29be7eef30bfe6d328b089baccb
# -----------------------------
df_orders['month_year'] = df_orders['order_date'].dt.to_period('M')
products_df['profit_ratio'] = products_df['marge'] / products_df['sales']

<<<<<<< HEAD
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
=======
# Merge orders + products + regions
df = df_orders.merge(products_df, on='product_name', how='left')
df = df.merge(df_regions, on='customer_id', how='left')

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("🔎 Filtres")

region_filter = st.sidebar.selectbox(
    "Région",
    ["Tous"] + sorted(df['region_name'].dropna().unique())
)

category_filter = st.sidebar.selectbox(
    "Catégorie",
    ["Tous"] + sorted(df['category'].dropna().unique())
)

period_filter = st.sidebar.selectbox(
    "Période (Mois-Année)",
    ["Tous"] + sorted(df['month_year'].astype(str).unique())
)

# Appliquer filtres
if region_filter != "Tous":
    df = df[df['region_name'] == region_filter]
if category_filter != "Tous":
    df = df[df['category'] == category_filter]
if period_filter != "Tous":
    df = df[df['month_year'].astype(str) == period_filter]

# -----------------------------
# KPIs
# -----------------------------
total_sales = df['sales'].sum()
total_profit = df['marge'].sum()
>>>>>>> 2794616986a5b29be7eef30bfe6d328b089baccb
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
<<<<<<< HEAD
sales_cat = df_filtered.groupby("category")["sales"].sum().reset_index()
=======
sales_cat = df.groupby("category")["sales"].sum().reset_index()
>>>>>>> 2794616986a5b29be7eef30bfe6d328b089baccb
fig1, ax1 = plt.subplots()
sns.barplot(data=sales_cat, x="category", y="sales", ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# -----------------------------
# Graph 2: Sales par mois
# -----------------------------
st.subheader("📈 Sales par mois")
<<<<<<< HEAD
sales_month = df_filtered.groupby("month_year")["sales"].sum().reset_index()
=======
sales_month = df.groupby("month_year")["sales"].sum().reset_index()
>>>>>>> 2794616986a5b29be7eef30bfe6d328b089baccb
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
<<<<<<< HEAD
ax3.pie(sales_cat['sales'], labels=sales_cat['category'], autopct='%1.1f%%', startangle=180)
=======
ax3.pie(
    sales_cat['sales'],
    labels=sales_cat['category'],
    autopct='%1.1f%%',
    startangle=90
)
>>>>>>> 2794616986a5b29be7eef30bfe6d328b089baccb
ax3.set_title("Répartition des ventes par catégorie")
st.pyplot(fig3)

# -----------------------------
# Graph 4: Top 10 produits
# -----------------------------
st.subheader("🏆 Top 10 produits")
<<<<<<< HEAD
top_products = df_filtered.groupby('product_name')['sales'].sum().nlargest(10).reset_index()
=======
top_products = df.groupby('product_name')['sales'].sum().nlargest(10).reset_index()
>>>>>>> 2794616986a5b29be7eef30bfe6d328b089baccb
fig4, ax4 = plt.subplots()
sns.barplot(data=top_products, x='sales', y='product_name', ax=ax4)
st.pyplot(fig4)

# -----------------------------
# Graph 5: Heatmap ventes par région et catégorie
# -----------------------------
st.subheader("🌡️ Heatmap ventes par région et catégorie")
<<<<<<< HEAD
pivot_table = df_filtered.pivot_table(values='sales', index='region_name', columns='category', aggfunc='sum')
=======
pivot_table = df.pivot_table(
    values='sales',
    index='region_name',
    columns='category',
    aggfunc='sum'
)
>>>>>>> 2794616986a5b29be7eef30bfe6d328b089baccb
fig5, ax5 = plt.subplots(figsize=(8,5))
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap="coolwarm", ax=ax5)
st.pyplot(fig5)

# -----------------------------
<<<<<<< HEAD
# Aperçu des données
# -----------------------------
st.subheader("📄 Aperçu des données")
st.dataframe(df_filtered.head())
=======
# Data preview
# -----------------------------
st.subheader("📄 Aperçu des données")
st.dataframe(df.head())
>>>>>>> 2794616986a5b29be7eef30bfe6d328b089baccb
