import streamlit as st
import requests

st.set_page_config(page_title="Scoring Crédit", layout="centered")

st.title("🔍 Prédiction de Risque de Crédit")
st.markdown("Remplis les champs ci-dessous pour prédire si un client est à risque ou non.")

# Champs utilisateur
credit_amount = st.number_input("Montant du crédit (€)", min_value=0, value=2500)
credit_purpose_car = st.checkbox("Crédit pour une voiture ?")
credit_purpose_other = st.checkbox("Crédit autre usage ?")
credit_history_critical = st.checkbox("Historique crédit critique ?")
status_single = st.checkbox("Le client est célibataire ?")
saving_status_low = st.checkbox("Épargne faible ? (< 100€)")

# Appel API
if st.button("🔮 Prédire"):
    payload = {
        "credit_amount": credit_amount,
        "credit_purpose_car": int(credit_purpose_car),
        "credit_history_critical": int(credit_history_critical),
        "status_single": int(status_single),
        "saving_status_low": int(saving_status_low),
        "credit_purpose_other": int(credit_purpose_other)
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()

        if "error" in result:
            st.error(f"Erreur : {result['error']}")
        else:
            prediction = "❌ Client à risque (bad)" if result["prediction"] == 1 else "✅ Client fiable (good)"
            proba = round(result["probability_bad"] * 100, 2)
            st.success(prediction)
            st.info(f"Probabilité d'être à risque : {proba} %")

    except requests.exceptions.ConnectionError:
        st.error("⚠️ L'API ne répond pas. Assure-toi que FastAPI tourne sur http://127.0.0.1:8000")
