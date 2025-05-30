import streamlit as st

st.title(":blue[Asistente virtual para el curso de Mejoramiento Animal] 🐎 🐂 🐷 🐐 🐑 🐔")

multi = '''Estos son los temas que se ven el curso:
Dinámica de poblaciones
Factores de corrección
Consanguinidad y parentesco genético
Heredabilidad y repetibilidad
Métodos de selección
Progreso genético

'''
st.markdown(multi)

st.image("https://cdn.slidesharecdn.com/ss_thumbnails/mejoramientogeneticoanimal-240418190359-8edceafb-thumbnail.jpg?width=560&fit=bounds")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.write(f"Hola, {nombre} 👋, bienvenido al curso de Mejoramiento Animal")

# Widget: slider
numero = st.slider("Indica cuál es tu dominio sobre el Mejoramiento Animal", min_value=0, max_value=5, value=10)
