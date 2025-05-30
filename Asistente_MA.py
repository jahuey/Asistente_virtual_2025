import streamlit as st

st.set_page_config(page_title="Asistente de Mejoramiento Genético", layout="centered")

st.title(":blue[Asistente virtual para el curso de Mejoramiento Animal] 🐎 🐂 🐷 🐐 🐑 🐔")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.success(f"Hola, {nombre} 👋, bienvenido al curso de Mejoramiento Animal")

nivel = st.slider("Indica cuál es tu dominio sobre el Mejoramiento Animal (0 = nada, 5 = experto)", 0, 5, 2)

st.image("https://cdn.slidesharecdn.com/ss_thumbnails/mejoramientogeneticoanimal-240418190359-8edceafb-thumbnail.jpg?width=560&fit=bounds")

# Diccionario vacío o con ejemplo para que tú lo llenes
temas_razonados = {
    "Dinámica de poblaciones": [
        # Aquí vas a pegar tus razonados, por ejemplo:
        # "Explica el efecto del tamaño efectivo de la población sobre la variabilidad genética.",
        # "¿Qué es la deriva genética y cómo se manifiesta en poblaciones pequeñas?"
    ],
    "Factores de corrección": [],
    "Consanguinidad y parentesco genético": [],
    "Heredabilidad y repetibilidad": [],
    "Metodologías actuales para la predicción de los valores de cría": [],
    "Métodos de selección": [],
    "Progreso genético": [],
    "Correlaciones y respuesta correlacionada": [],
    "Selección por más de una característica": [],
    "Depresión endogámica": [],
    "Cruzamientos": []
}

st.subheader("📘 Temas del curso y razonados disponibles")

for tema in temas_razonados:
    with st.expander(f"🔹 {tema}"):
        razonados = temas_razonados[tema]
        if razonados:
            for i, razonado in enumerate(razonados, 1):
                st.markdown(f"**{i}.** {razonado}")
        else:
            st.info("Aún no se han cargado razonados para este tema. Puedes agregarlos desde el código.")

