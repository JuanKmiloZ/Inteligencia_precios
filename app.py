import streamlit as st
from data import cargar_datos
from model import entrenar_modelo

st.title("💍 Inteligencia de Precios en Joyería")

# --- Cargar datos ---
df = cargar_datos()
df = df.dropna(subset=["precio", "peso", "quilates"])
df["quilates"] = df["quilates"].replace(0, df["quilates"].mean())

st.subheader("Datos recientes")
st.write(df.head())

# --- Modelo ---
model, mse, r2, resultados = entrenar_modelo()

st.subheader("📊 Métricas")
st.metric("MSE", f"{mse:.2f}")
st.metric("R²", f"{r2:.4f}")

st.subheader("Predicciones vs reales")
st.dataframe(resultados.head())

# --- Gráfico precios promedio por tienda ---
st.subheader("📈 Precio promedio por tienda")
df_grouped = df.groupby("tienda")["precio"].mean().reset_index()
st.bar_chart(df_grouped.set_index("tienda"))
