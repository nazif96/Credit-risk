# Analyse et Prédiction du Risque de Crédit

## 📖Contexte 
Dans le climat économique actuel, l'analyse du risque de crédit est plus pertinente que jamais. Les institutions financières sont continuellement confrontées au défi de distinguer les bons emprunteurs des mauvais pour minimiser les pertes tout en maximisant les opportunités de revenus.

## 🎯 Objectif 

L'objectif de ce projet était de développer un modèle prédictif capable de classer les statuts de compte courant des clients en "bon" ou "mauvais" en fonction de leur risque de crédit. En utilisant un ensemble de données comprenant 1000 clients. 

## 🏗️ Structure du projet 

```
Risque_credit/
│
├── Data/
│   ├── Credit_cleaned.csv       # Base de données propre en format csv 
│   ├── Credit_cleaned.json      # Base de données propre en format csv
│   ├── dataset.csv              # Base de données brute
│   └── df_api.csv               # Base de données pour l'api  
|
├── images/                      # images des visualisations
│   

├── model_API/
│   ├── features                 # Liste des 6 features utilisées
│   ├── log_reg.pkl              # Modèle de régression logistique sauvegardé
│   ├── main.py                  # API FastAPI avec route /predict 
│   ├── scaler1.pkl              # Scaler entraîné sur credit_amount 
│
├── Model_training/
│   └── train_model.py           # entrainement du model logistic regression
|
├── streamlit_app/
│   └── app.py                   # Interface utilisateur pour prédiction
│
├── LICENSE 
├── README.md                    # Description du projet
└── requirements.txt             # Dépendances à installer
``` 
