# Dashboard Commercial Interactif

## Contexte du projet
Après avoir nettoyé, structuré et stocké les données dans PostgreSQL, l’entreprise souhaite exploiter ces données via un dashboard interactif. L'objectif est d'aider les décideurs à analyser la performance commerciale en offrant une vision synthétique des KPIs et des analyses comparatives par région, catégorie et période.

Le dashboard permet également d'explorer les données via des filtres interactifs pour mieux comprendre la performance des ventes et de la rentabilité.

## Objectifs
- Se connecter à PostgreSQL depuis Python
- Extraire les données nécessaires via des requêtes SQL
- Calculer des statistiques descriptives
- Construire des KPIs métier (Total Sales, Total Profit, Average Profit Margin)
- Créer des visualisations avec matplotlib et seaborn
- Développer un dashboard interactif avec filtres
- Suivre le projet via Jira

## User Story
En tant qu’équipe Data Analysts, nous devons développer un dashboard interactif permettant aux équipes métiers d’analyser la performance des ventes et la rentabilité.

## Ressources
- Base PostgreSQL : `superstore_db`
- Langages et bibliothèques : Python 3.x, Streamlit, SQLAlchemy, matplotlib, seaborn, pandas
- IDE : Jupyter Notebook / VS Code / PyCharm
- Suivi projet : Jira

## Installation et configuration
1. Cloner le dépôt ou copier le fichier `dashboard.py`.
2. Installer les dépendances :
```bash
pip install streamlit pandas sqlalchemy psycopg2-binary matplotlib seaborn python-dotenv

