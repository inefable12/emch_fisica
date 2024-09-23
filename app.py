import streamlit as st
import random

# Función para generar un tipo de ejercicio aleatorio
def generar_ejercicio():
    tipo = random.choice(["fuerza", "masa", "aceleracion"])
    masa = random.uniform(1, 100)  # Masa entre 1 y 100 kg
    aceleracion = random.uniform(0.1, 10)  # Aceleración entre 0.1 y 10 m/s^2
    fuerza = masa * aceleracion  # Fuerza según la segunda ley de Newton
    return tipo, masa, aceleracion, fuerza

# Título de la app
st.title("Generador de Ejercicios de la Segunda Ley de Newton")

# Botón para generar el ejercicio
if st.button("Generar Ejercicio"):
    tipo, masa, aceleracion, fuerza = generar_ejercicio()
    st.session_state.tipo = tipo  # Guardar el tipo de ejercicio
    st.session_state.masa = masa  # Guardar la masa
    st.session_state.aceleracion = aceleracion  # Guardar la aceleración
    st.session_state.fuerza = fuerza  # Guardar la fuerza

    if tipo == "fuerza":
        st.write(f"Ejercicio generado: Calcula la fuerza (F).")
        st.write(f"Masa (m): {masa:.2f} kg")
        st.write(f"Aceleración (a): {aceleracion:.2f} m/s²")
    elif tipo == "masa":
        st.write(f"Ejercicio generado: Calcula la masa (m).")
        st.write(f"Fuerza (F): {fuerza:.2f} N")
        st.write(f"Aceleración (a): {aceleracion:.2f} m/s²")
    else:  # tipo == "aceleracion"
        st.write(f"Ejercicio generado: Calcula la aceleración (a).")
        st.write(f"Fuerza (F): {fuerza:.2f} N")
        st.write(f"Masa (m): {masa:.2f} kg")

# Botón para mostrar la respuesta
if st.button("Mostrar Respuesta"):
    if "tipo" in st.session_state:
        tipo = st.session_state.tipo
        if tipo == "fuerza":
            st.write(f"La fuerza (F) es: {st.session_state.fuerza:.2f} N")
        elif tipo == "masa":
            masa = st.session_state.fuerza / st.session_state.aceleracion
            st.write(f"La masa (m) es: {masa:.2f} kg")
        else:  # tipo == "aceleracion"
            aceleracion = st.session_state.fuerza / st.session_state.masa
            st.write(f"La aceleración (a) es: {aceleracion:.2f} m/s²")
    else:
        st.write("Primero debes generar un ejercicio.")
