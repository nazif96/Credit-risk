# Analyse et Prédiction du Risque de Crédit

## 📖Contexte 
Dans le climat économique actuel, l'analyse du risque de crédit est plus pertinente que jamais. Les institutions financières sont continuellement confrontées au défi de distinguer les bons emprunteurs des mauvais pour minimiser les pertes tout en maximisant les opportunités de revenus.

## 🎯 Objectif 

L'objectif de ce projet était de développer un modèle prédictif capable de classer les statuts de compte courant des clients en "bon" ou "mauvais" en fonction de leur risque de crédit. En utilisant un ensemble de données comprenant 1000 clients. 

## 🏗️ Structure du projet 

Risque_credit/
│
├── model_training/
│   ├── train_model.py              # Script d'entraînement + sauvegarde modèle/scaler/features
│   └── (ou un notebook Jupyter)
│
├── model_API/
│   ├── main.py                     # API FastAPI avec route /predict
│   ├── logistic_model.pkl          # Modèle de régression logistique sauvegardé
│   ├── scaler.pkl                  # Scaler entraîné sur credit_amount
│   ├── features_columns.pkl        # Liste des 6 features utilisées
│
├── streamlit_app/
│   └── app.py                      # Interface utilisateur pour prédiction
│
├── requirements.txt                # Dépendances à installer (voir ci-dessous)
└── README.md                       # (optionnel) description du projet
