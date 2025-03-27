from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Initialisation de l'app
app = FastAPI(title="API - Crédit Logistic Regression")

# Chargement du modèle, scaler et colonnes utilisées
model = joblib.load("log_reg.pkl")
scaler = joblib.load("scaler1.pkl")
features = joblib.load("features_columns1.pkl")  # ['credit_amount', ..., etc.]

# Classe d'entrée avec les 6 variables utilisées
class InputData(BaseModel):
    credit_amount: float
    credit_purpose_car: int = 0
    credit_history_critical: int = 0
    status_single: int = 0
    saving_status_low: int = 0
    credit_purpose_other: int = 0

# Fonction de préparation des données
def prepare_input(data_dict, expected_columns):
    df = pd.DataFrame([data_dict])

    # Ajouter les colonnes manquantes
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0

    # Réordonner
    df = df[expected_columns]

    # Normalisation uniquement sur credit_amount
    df[['credit_amount']] = scaler.transform(df[['credit_amount']])

    return df

# Accueil
@app.get("/")
def home():
    return {
        "message": "Bienvenue sur l'API scoring crédit (Logistic Regression)",
        "status": "✅ Prête",
        "test": "/docs"
    }

# Route prédiction
@app.post("/predict")
def predict(data: InputData):
    try:
        data_dict = data.dict()
        df_prepared = prepare_input(data_dict, features)
        prediction = model.predict(df_prepared)[0]
        proba = model.predict_proba(df_prepared)[0][1]

        return {
            "prediction": int(prediction),
            "probability_bad": round(proba, 3)
        }
    except Exception as e:
        return {"error": str(e)}
