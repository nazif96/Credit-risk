# Analyse et Prédiction du Risque de Crédit

## 📖Contexte 
Dans le climat économique actuel, l'analyse du risque de crédit est plus pertinente que jamais. Les institutions financières sont continuellement confrontées au défi de distinguer les bons emprunteurs des mauvais pour minimiser les pertes tout en maximisant les opportunités de revenus.

## 🎯 Objectif 

L'objectif de ce projet était de développer un modèle prédictif capable de classer les statuts de compte courant des clients en "bon" ou "mauvais" en fonction de leur risque de crédit. En utilisant un ensemble de données comprenant 1000 clients. 

## 🏗️ Structure du projet 

Le projet est organisé comme suit:
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
│   └── scaler1.pkl              # Scaler entraîné sur credit_amount 
│
├── Model_training/
│   └── train_model.py 
|
├── Notebooks/
│   ├── app.ipynb                # Notebook de regression log_reg pour l'api et streamlit 
│   ├── Cleannig_data.ipynb      # Notebook de nettoyage des données brutes
│   ├── EDA.ipynb                # Analyse exploratoire des données
│   └── Preprocess_Ml.ipynb      # Prétraitement et Machine Learning sur les données 
|
├── streamlit_app/
│   └── app.py                   # Interface utilisateur pour prédiction
│
├── LICENSE 
├── README.md                    # Description du projet
└── requirements.txt             # Dépendances à installer
``` 
## Analyse Exploratoire des Données 

### 1. Data cleaning `Cleaning_data.ipynb`
Importation, nettoyage des données et sauvegarde des données propres dans un fichier csv `Credit_cleaned.csv` et un fichier json `Credit_cleaned.csv` 

### 2.📊 Analyse exploratoire des données `EDA.ipynb`

-  Statistiques descriptives
```
|       Statistiques       | Durations | Credit amount  | Installment_Rate_Percent  | Residence_Years  | Age in years  | Num_Existing_Credits   | Liable_People  |
|-------------------------:|----------:|---------------:|--------------------------:|-----------------:|--------------:|-----------------------:|---------------:|
| **count**                | 1000.00   | 1000.00        | 1000.00                   | 1000.00          | 1000.00       | 1000.00                | 1000.00        |
| **mean**                 | 20.90     | 3271.26        | 2.97                      | 2.85             | 35.55         | 1.41                   | 1.16           |
| **std**                  | 12.06     | 2822.74        | 1.12                      | 1.10             | 11.38         | 0.58                   | 0.36           |
| **min**                  | 4.00      | 250.00         | 1.00                      | 1.00             | 19.00         | 1.00                   | 1.00           |
| **25%** (1er quartile)   | 12.00     | 1365.50        | 2.00                      | 2.00             | 27.00         | 1.00                   | 1.00           |
| **50%** (médiane)        | 18.00     | 2319.50        | 3.00                      | 3.00             | 33.00         | 1.00                   | 1.00           |
| **75%** (3e quartile)    | 24.00     | 3972.25        | 4.00                      | 4.00             | 42.00         | 2.00                   | 1.00           |
| **max**                  | 72.00     | 18424.00       | 4.00                      | 4.00             | 75.00         | 4.00                   | 2.00           |

```


-  Analyses univariés 

    *variable cible* 
    ![target](https://github.com/nazif96/Credit-risk/blob/main/images/account_status.png) 

    *Le genre et status marital*
    ![Genre_status](https://github.com/nazif96/Credit-risk/blob/main/images/genre_statut.png)

    *plus*
     ![Autres](https://github.com/nazif96/Credit-risk/blob/main/Notebooks/EDA.ipynb)

- analyses bivarié 
