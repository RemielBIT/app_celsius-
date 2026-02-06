import streamlit as st

st.set_page_config(
    page_title="Conversor Celsius a Fahrenheit",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Conversor de Temperatura")
st.write("Ingresa los grados Celsius y conviértelos a Fahrenheit")

celsius = st.number_input(
    "Grados Celsius (°C)",
    value=0.0,
    step=0.1
)

fahrenheit = (celsius * 9/5) + 32

st.success(f"🔥 {celsius} °C = {fahrenheit:.2f} °F")
