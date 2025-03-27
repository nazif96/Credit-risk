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
│   ├── features_columns1.pkl    # Liste des 6 features utilisées
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

-  **Statistiques descriptives**
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

-  **Analyses univariés** 

    *variable cible* 
    ![target](https://github.com/nazif96/Credit-risk/blob/main/images/account_status.png) 

    *Le genre et status marital*
    ![Genre_status](https://github.com/nazif96/Credit-risk/blob/main/images/genre_statut.png)

    
    ![Plus](https://github.com/nazif96/Credit-risk/blob/main/Notebooks/EDA.ipynb)

- **Analyses bivariés** 

    *Variable cible vs montant de crédit*
    ![](https://github.com/nazif96/Credit-risk/blob/main/images/target_vs_amount.png)

    *Montant de crédit vs le but de crédit &  Age vs Job *
    ![Job_age_purpose_amount](https://github.com/nazif96/Credit-risk/blob/main/images/output.png)

    ![Plus](https://github.com/nazif96/Credit-risk/blob/main/Notebooks/EDA.ipynb)

- **Corrélation**

    *Variables numériques*

    ![corr_num](https://github.com/nazif96/Credit-risk/blob/main/images/corr_num_var.png)

    *Variables catégorielles* 

    ![corr_cat](https://github.com/nazif96/Credit-risk/blob/main/images/corr_cat_var.png) 


## Prétraitement et Entraînement des modèles `Preprocess_ML.ipynb`

Sélection des variables pertinentes et prétraitement des données pour l'apprentissage automatique

-surechantillonnage de la variable cible `Checking_Account_Status` avec la methode *SMOTE* pour corriger le deséquilibre des modalités 

- Modèles 
  - Logistic Regression
  - Random Forest
  - Decision Tree
  - XGBoost


**Evaluations des mode=èles (Metrics)** 

✅ Comparaison des performances des modèles (classe "bad" = 1)

| Modèle              | Accuracy | Precision (1)  | Recall (1)  | F1-score (1)  |
|--------------------:|---------:|---------------:|------------:|--------------:|
| Logistic Regression | 0.685    | 0.47           | 0.56        | 0.51          |
| Random Forest       | 0.665    | 0.40           | 0.29        | 0.34          |
| Decision Tree       | 0.635    | 0.40           | 0.47        | 0.43          |
| XGBoost             | 0.690    | 0.47           | 0.39        | 0.43          |

**Visualisation**

![Modeles](https://github.com/nazif96/Credit-risk/blob/main/images/modeles.png)

**Courbe ROC**

![ROC](https://github.com/nazif96/Credit-risk/blob/main/images/roc.png)

**Meilleur Modèle** : Le modèle final sélectionné est une régression logistique 
Pour plus de détails, consultez le notebook notebooks/Preprocess_ML.ipynb.

**Top features de la régression logistique**

![Top15](https://github.com/nazif96/Credit-risk/blob/main/images/Top_Features.png)

## Creation d'un API (Fastapi)

- rentraînement du modèle logistic regression `App.ipynb` avec quelques variables plus pertienentes puis sauvegarde en `log_reg.pkl`
- sauvegarde des features pour le training de log_reg  en `scaler1.pkl`
- Sauvegarde Scaler entraîné sur credit_amount  en `features_columns1.pkl`

Puis **Création d'un api**

## ⚙️ Installation 

**Prérequis**

- Python 3.12+
- Pip pour gérer les packages 

**Etapes d'Installation**

1. Clonez le dépôt 

```bash 
git clone https://github.com/nazif96/Credit-risk.git
cd Credit-risk
```

2. Créez un environnement virtuel :

```bash 
python -m venv venv 
```

3. Activez l'environnement

```bash 
.\env\Scripts\activate
```

4. Installez les dépendances

```bash 
pip install -r requirements.txt
```
## 🚀 Utilisation (local)

1. Étape 1 — Lancer l'API FastAPI

```bash 
cd model_API
uvicorn main:app --reload
```

- Tu verras : Uvicorn running on http://127.0.0.1:8000

- Tu peux tester l’API sur Swagger : http://127.0.0.1:8000/docs

     clique sur POST/predict puis sur `try it out ` 
     éditer les json puis clique sur *Execut*

![](https://github.com/nazif96/Credit-risk/blob/main/images/api1_swagger.png)

**NB** Laisse ce terminal ouvert pendant toute la session (ne le ferme pas)

2. Étape 2 — Lancer l'application Streamlit

Dans un nouveau terminal, va dans le dossier et lancer l'interface streamlit.

```bash 
cd streamlit_app
streamlit run app.py
```
![inter_streamlit](https://github.com/nazif96/Credit-risk/blob/main/images/inter1.png)

L’app va s’ouvrir automatiquement dans ton navigateur sur : 👉 http://localhost:8501
