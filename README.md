📊 Dashboard Interactif – Analyse des Ventes
📝 Contexte du projet

L’entreprise a nettoyé et structuré ses données dans PostgreSQL et souhaite désormais exploiter ces informations via un dashboard interactif.

L’objectif est de fournir aux équipes métiers :

Une vision synthétique des KPIs
Des analyses comparatives par région, catégorie et période
Des indicateurs statistiques simples pour comprendre la performance
Un outil interactif pour filtrer et explorer les données

Ce projet s’inscrit dans la phase Data Visualization & Data Storytelling.

🎯 Objectifs
Se connecter à PostgreSQL depuis Python
Extraire les données via requêtes SQL
Calculer des statistiques descriptives
Construire des KPIs métier
Créer des visualisations interactives avec matplotlib et seaborn
Développer un dashboard Streamlit
Suivre le projet via Jira
👥 User Story

En tant qu’équipe Data Analysts, nous devons développer un dashboard interactif permettant aux équipes métiers d’analyser la performance des ventes et la rentabilité.

🛠 Technologies utilisées
Base de données : PostgreSQL (superstore_db)
Langage : Python 3.x
Librairies : pandas, SQLAlchemy, psycopg2, matplotlib, seaborn, streamlit
IDE : Jupyter Notebook / VS Code / PyCharm
Suivi projet : Jira
🚀 Étapes principales
#1 Connexion à PostgreSQL
Connexion via SQLAlchemy ou psycopg2
Lecture des tables nécessaires
Vérification de la cohérence et complétude des données
#2 Préparation des données
Création de DataFrames pandas
Calcul des métriques clés : Total Sales, Total Profit, Profit Margin, Quantité vendue
Calcul des statistiques de base : moyenne, médiane, min, max, écart-type
#3 Feature engineering
Création de colonnes dérivées (ex. mois-année, profit ratio)
Agrégation des données pour graphiques par période, région et catégorie
Identification des top 10 produits ou clients
#4 Création des visualisations
Graphiques : barres, lignes, secteurs, combinés (ventes vs profit)
Heatmaps et distributions avec seaborn
Filtres interactifs :
Région
Catégorie de produit
Période (année, mois…)
#5 Construction du dashboard Streamlit
KPIs principaux : Total Sales, Total Profit, Average Profit Margin
Graphiques interactifs avec filtres
Vérification de la lisibilité et de l’interactivité
Tests complets pour toutes les métriques et filtres
#6 Lancement du projet
Installer les dépendances :
pip install streamlit pandas sqlalchemy psycopg2-binary matplotlib seaborn python-dotenv
Créer un fichier .env à la racine :
DB_USER=ton_utilisateur
DB_PASSWORD=ton_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
DB_NAME=superstore_db
Lancer le dashboard :
streamlit run dashboard.py
