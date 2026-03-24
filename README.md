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

## Créer un fichier .env à la racine et définir les variables suivantes :
DB_USER=ton_utilisateur
DB_PASSWORD=ton_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
DB_NAME=superstore_db
Lancement du dashboard

## Pour lancer le dashboard Streamlit :

streamlit run dashboard.py

## Fonctionnalités principales
## KPIs principaux :
 Total Sales, Total Profit, Profit Margin
## Filtres interactifs :
  Région, Catégorie, Période (Mois-Année)
## Visualisations :
Bar chart : Ventes par catégorie
Line chart : Ventes par mois
Pie chart : Répartition des ventes par catégorie
Top 10 produits
Heatmap : Ventes par région et catégorie
Aperçu des données : Table interactive pour inspecter les premières lignes

## Étapes principales du projet
- Connexion à PostgreSQL et extraction des données
- Préparation et nettoyage des données
- Feature engineering : mois-année, profit ratio, top produits et clients
- Création des visualisations avec matplotlib et seaborn
- Construction du dashboard interactif avec Streamlit
- Test et validation de la lisibilité, filtres et KPIs
- Préparation des livrables et documentation pour l’utilisateur
