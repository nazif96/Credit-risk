
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# 1. Charger tes données
df = pd.read_csv("donnees.csv")  # Remplace par le bon nom de fichier

# 2. Nettoyage des colonnes
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 3. Regroupements manuels (si pas déjà faits dans le CSV)
df['credit_purpose_grouped'] = df['credit_purpose'].replace({
    'radio/tv': 'electronics',
    'domestic appliance': 'electronics',
    'furniture/equipment': 'household',
    'repairs': 'household',
    'new car': 'car',
    'used car': 'car',
    'education': 'education',
    'retraining': 'education',
    'business': 'business',
    'other': 'other'
})

df['credit_history_grouped'] = df['credit_history'].replace({
    'no credits/all paid': 'good',
    'all paid': 'good',
    'existing paid': 'average',
    'delayed previously': 'poor',
    'critical/other existing credit': 'critical'
})

df['status_grouped'] = df['status'].replace({
    'single': 'single',
    'div/dep/mar': 'not_single',
    'mar/wid': 'not_single',
    'div/sep': 'not_single'
})

df['saving_status_grouped'] = df['saving_status'].replace({
    'no savings': 'low',
    'less than 100': 'low',
    '100-500': 'medium',
    '500-1000': 'high',
    'more than 1000': 'high'
})

# 4. Préparation des données finales
df['account_status'] = df['checking_account_status'].apply(lambda x: 1 if x == 'bad' else 0)
y = df['account_status']

# On garde uniquement les colonnes utiles
df = df[[
    'credit_amount', 'credit_purpose_grouped', 'credit_history_grouped',
    'status_grouped', 'saving_status_grouped', 'account_status'
]]

# 5. Normalisation de la variable numérique
scaler = StandardScaler()
df['credit_amount'] = scaler.fit_transform(df[['credit_amount']])

# 6. Encodage one-hot
df = pd.get_dummies(df, columns=[
    'credit_purpose_grouped', 'credit_history_grouped',
    'status_grouped', 'saving_status_grouped'
], drop_first=True)

# 7. Sélection des features finales (6 variables)
features = [
    'credit_amount',
    'credit_purpose_grouped_car',
    'credit_purpose_grouped_other',
    'credit_history_grouped_critical',
    'status_grouped_single',
    'saving_status_grouped_low'
]
X = df[features]

# 8. Split + entraînement
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# 9. Sauvegarde
joblib.dump(model, "../model_API/logistic_model.pkl")
joblib.dump(scaler, "../model_API/scaler.pkl")
joblib.dump(features, "../model_API/features_columns.pkl")

print("✅ Modèle, scaler et features sauvegardés avec succès.")
