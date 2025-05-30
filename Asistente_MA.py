import streamlit as st
import openai

# Configura tu clave API
openai.api_key = "TU_API_KEY_AQUI"

# Título e introducción
st.title(":blue[Asistente virtual para el curso de Mejoramiento Animal] 🐎 🐂 🐷 🐐 🐑 🐔")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.write(f"Hola, {nombre} 👋, bienvenido al curso de Mejoramiento Animal")

# Slider corregido
nivel = st.slider("Indica cuál es tu dominio sobre el Mejoramiento Animal (0 = nada, 5 = experto)", 0, 5, 2)

st.image("https://cdn.slidesharecdn.com/ss_thumbnails/mejoramientogeneticoanimal-240418190359-8edceafb-thumbnail.jpg?width=560&fit=bounds")

# Temario
st.markdown("""
Estos son los temas que se ven en el curso:  
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
""")

# Razonados resueltos (puedes sustituir esto por un archivo externo luego)
razonados = """
1. Un toro tiene un valor genético de +30 kg para peso al destete y se aparea con una vaca cuyo valor es +20 kg. ¿Cuál es el valor genético esperado de la cría?
→ Respuesta: (30 + 20) / 2 = 25 kg.

2. Se desea calcular la heredabilidad de una característica con varianza genética de 15 y varianza fenotípica de 60.
→ Respuesta: h² = 15 / 60 = 0.25.

3. ¿Qué es la consanguinidad y cómo afecta al progreso genético?
→ Respuesta: Es la reproducción entre individuos emparentados genéticamente. Puede reducir la variabilidad genética y provocar depresión endogámica.
"""

# Sección del asistente virtual
st.subheader("🤖 Asistente virtual")

pregunta = st.text_input("Escribe aquí tu duda sobre los temas del curso o algún razonado:")

if pregunta:
    with st.spinner("Consultando al asistente..."):
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en mejoramiento genético animal que responde preguntas usando los razonados resueltos como referencia."},
                {"role": "user", "content": f"Aquí están los razonados:\n{razonados}\n\nPregunta del estudiante: {pregunta}"}
            ],
            temperature=0.7,
            max_tokens=500
        )
        st.success(respuesta.choices[0].message["content"])
