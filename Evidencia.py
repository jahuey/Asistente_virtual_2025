import streamlit as st

st.title(":blue[Asistente virtual para el curso de Mejoramiento Animal] 🐎 🐂 🐷 🐐 🐑 🐔")

multi = '''Estos son los temas que se ven el curso:  
* Dinámica de poblaciones  
* Factores de corrección  
* Consanguinidad y parentesco genético  
* Heredabilidad y repetibilidad  
* Metodologías actuales para la predicción de los valores de cría  
* Métodos de selección  
* Progreso genético  
* Correlaciones y respuesta correlacionada  
* Selección por más de una característica  
* Depresión endogámica  
* Cruzamientos
'''

st.write(multi)

st.image("https://cdn.slidesharecdn.com/ss_thumbnails/mejoramientogeneticoanimal-240418190359-8edceafb-thumbnail.jpg?width=560&fit=bounds")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.write(f"Hola, {nombre} 👋, bienvenido al curso de Mejoramiento Animal")

# Widget: slider
numero = st.slider("Indica cuál es tu dominio sobre el Mejoramiento Animal", min_value=0, max_value=5, value=10)
