import streamlit as st
import random

# Función para generar un ejercicio aleatorio
def generar_ejercicio():
    masa = random.uniform(1, 100)  # Masa entre 1 y 100 kg
    aceleracion = random.uniform(0.1, 10)  # Aceleración entre 0.1 y 10 m/s^2
    return masa, aceleracion

# Función para calcular la fuerza
def calcular_fuerza(masa, aceleracion):
    return masa * aceleracion

# Título de la app
st.title("Generador de Ejercicios de la Segunda Ley de Newton")

# Botón para generar el ejercicio
if st.button("Generar Ejercicio"):
    masa, aceleracion = generar_ejercicio()
    st.session_state.masa = masa  # Guardar la masa
    st.session_state.aceleracion = aceleracion  # Guardar la aceleración
    st.write(f"Ejercicio generado:")
    st.write(f"Masa (m): {masa:.2f} kg")
    st.write(f"Aceleración (a): {aceleracion:.2f} m/s²")

# Botón para mostrar la respuesta
if st.button("Mostrar Respuesta"):
    if "masa" in st.session_state and "aceleracion" in st.session_state:
        fuerza = calcular_fuerza(st.session_state.masa, st.session_state.aceleracion)
        st.write(f"La fuerza aplicada (F) es: {fuerza:.2f} N")
    else:
        st.write("Primero debes generar un ejercicio.")

