import streamlit as st

st.set_page_config(page_title="Asistente de Mejoramiento Genético", layout="wide")

st.title(":blue[Asistente virtual para el curso de Mejoramiento Animal] 🐎 🐂 🐷 🐐 🐑 🐔")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.success(f"Hola, {nombre} 👋, bienvenido al curso de Mejoramiento Animal")

nivel = st.slider("Indica cuál es tu dominio sobre el Mejoramiento Animal (0 = nada, 5 = experto)", 0, 5, 2)

# Diccionario de razonados por tema (aún vacíos)
temas_razonados = {
    "Dinámica de poblaciones": [],
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

# Divide la pantalla en 2 columnas: izquierda (más ancha) y derecha
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📘 Selecciona un tema:")
    for tema in temas_razonados:
        if st.button(tema, use_container_width=True):
            st.markdown(f"### 🧠 Razonados de: {tema}")
            razonados = temas_razonados[tema]
            if razonados:
                for i, r in enumerate(razonados, 1):
                    st.markdown(f"**{i}.** {r}")
            else:
                st.info("Aún no hay razonados cargados para este tema.")
            st.markdown("---")

with col2:
    st.image("https://cdn.slidesharecdn.com/ss_thumbnails/mejoramientogeneticoanimal-240418190359-8edceafb-thumbnail.jpg?width=560&fit=bounds")

