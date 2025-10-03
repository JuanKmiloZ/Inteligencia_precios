import streamlit as st
from model import entrenar_modelo

st.set_page_config(page_title="Inteligencia de Precios", layout="wide")

st.title("💍 Inteligencia de Precios en Joyería")
st.markdown("Comparación de precios y predicción de valores en el mercado.")

# Entrenar y obtener resultados
model, mse, r2, resultados = entrenar_modelo()

st.subheader("📊 Métricas del modelo")
col1, col2 = st.columns(2)
with col1:
    st.metric("MSE", f"{mse:.2f}")
with col2:
    st.metric("R²", f"{r2:.4f}")

st.subheader("🔮 Predicciones vs Valores reales")
st.dataframe(resultados.head(10))
