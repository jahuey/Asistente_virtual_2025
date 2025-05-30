import streamlit as st

st.title(":blue[Asistente virtual para el curso de Mejoramiento Animal] 🐎 🐂 🐷 🐐 🐑 🐔")

st.image("https://cdn.slidesharecdn.com/ss_thumbnails/mejoramientogeneticoanimal-240418190359-8edceafb-thumbnail.jpg?width=560&fit=bounds")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.write(f"Hola, {nombre} 👋, bienvenido al curso de Mejoramiento Animal")

# Widget: slider
numero = st.slider("Indica cual es tu dominio de la materia", min_value=0, max_value=10, value=50)
