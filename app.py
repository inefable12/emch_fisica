import streamlit as st
import random

###########################################################
st.sidebar.image("Recursos/EUdpC.gif",
                 caption="Recursos para Física General")

####################### Pag 1 #############################
def generar_ejercicio1():
    ejercicios = [
        "Un automóvil está parado en un semáforo.",
        "Una pelota rueda en una superficie lisa a velocidad constante.",
        "Un avión vuela en línea recta a velocidad constante.",
        "Una caja está en reposo sobre una mesa.",
        "Una persona está sentada sin moverse en una silla.",
        "Un objeto flota inmóvil en el espacio exterior.",
        "Un tren se desplaza a velocidad constante en una vía recta."
    ]
    ejercicio = random.choice(ejercicios)
    return ejercicio

def Home():
    st.title("Ejercicios de la Primera Ley de Newton")
    # Botón para generar el ejercicio
    if st.button("Generar Ejercicio"):
        ejercicio = generar_ejercicio1()
        st.session_state.ejercicio = ejercicio
        st.write(f"Ejercicio generado:")
        st.write(ejercicio)
    # Botón para mostrar la respuesta
    if st.button("Mostrar Respuesta"):
        if "ejercicio" in st.session_state:
            ejercicio = st.session_state.ejercicio
            # Mostrar la respuesta correcta basada en el ejercicio generado
            if "parado" in ejercicio or "reposo" in ejercicio or "inmóvil" in ejercicio:
                st.write("Respuesta: El objeto está en reposo. No hay fuerza neta actuando sobre él.")
            else:
                st.write("Respuesta: El objeto se mueve con velocidad constante. No hay fuerza neta actuando sobre él.")
        else:
            st.write("Primero debes generar un ejercicio.")

######################## Pag 2 ############################
def page2():
    def generar_ejercicio2():
    tipo = random.choice(["fuerza", "masa", "aceleracion"])
    masa = random.uniform(1, 100)  # Masa entre 1 y 100 kg
    aceleracion = random.uniform(0.1, 10)  # Aceleración entre 0.1 y 10 m/s^2
    fuerza = masa * aceleracion  # Fuerza según la segunda ley de Newton
    return tipo, masa, aceleracion, fuerza
    
    # Título de la app
    st.title("Generador de Ejercicios de la Segunda Ley de Newton")
    
    # Botón para generar el ejercicio
    if st.button("Generar Ejercicio"):
    tipo, masa, aceleracion, fuerza = generar_ejercicio2()
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

def page3():
    def generar_ejercicio():
        ejercicios = [
            "Un nadador empuja el agua hacia atrás con sus brazos.",
            "Una persona empuja una pared.",
            "Un cohete expulsa gases hacia abajo mientras despega.",
            "Un libro descansa sobre una mesa.",
            "Un caballo tira de una carreta.",
            "Una pelota golpea el suelo al caer.",
            "Un imán atrae una pieza de hierro."
        ]
        ejercicio = random.choice(ejercicios)
        return ejercicio
    
    # Título de la app
    st.title("Ejercicios de la Tercera Ley de Newton")
    
    # Botón para generar el ejercicio
    if st.button("Generar Ejercicio"):
        ejercicio = generar_ejercicio()
        st.session_state.ejercicio = ejercicio
        st.write(f"Ejercicio generado:")
        st.write(ejercicio)
    
    # Botón para mostrar la respuesta
    if st.button("Mostrar Respuesta"):
        if "ejercicio" in st.session_state:
            ejercicio = st.session_state.ejercicio
            # Mostrar la respuesta correcta basada en el ejercicio generado
            if "empuja el agua" in ejercicio:
                st.write("Respuesta: El nadador empuja el agua hacia atrás (acción), y el agua empuja al nadador hacia adelante (reacción).")
            elif "persona empuja una pared" in ejercicio:
                st.write("Respuesta: La persona empuja la pared (acción), y la pared empuja a la persona con una fuerza de igual magnitud en la dirección opuesta (reacción).")
            elif "expulsa gases" in ejercicio:
                st.write("Respuesta: El cohete expulsa gases hacia abajo (acción), y los gases empujan al cohete hacia arriba (reacción).")
            elif "libro descansa" in ejercicio:
                st.write("Respuesta: El libro ejerce una fuerza hacia abajo sobre la mesa (acción), y la mesa ejerce una fuerza de igual magnitud hacia arriba sobre el libro (reacción).")
            elif "caballo tira" in ejercicio:
                st.write("Respuesta: El caballo tira de la carreta hacia adelante (acción), y la carreta ejerce una fuerza de igual magnitud hacia atrás sobre el caballo (reacción).")
            elif "pelota golpea" in ejercicio:
                st.write("Respuesta: La pelota ejerce una fuerza hacia abajo sobre el suelo (acción), y el suelo ejerce una fuerza hacia arriba sobre la pelota (reacción).")
            elif "imán atrae" in ejercicio:
                st.write("Respuesta: El imán ejerce una fuerza de atracción sobre el hierro (acción), y el hierro ejerce una fuerza de igual magnitud hacia el imán (reacción).")
        else:
            st.write("Primero debes generar un ejercicio.")

################################################################### 
##########################Configuracion############################    
###################################################################    

page_names_to_funcs = {
  "1ra": Home,
  "2da": page2,
  "3ra": page3,
}

selected_page = st.sidebar.selectbox("Tipoa", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
    
