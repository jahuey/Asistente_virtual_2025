import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Asistente de Mejoramiento Genético", layout="centered")

st.title(":blue[Asistente virtual para el curso de Mejoramiento Animal] 🐎 🐂 🐷 🐐 🐑 🐔")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.success(f"Hola, {nombre} 👋, bienvenido al curso de Mejoramiento Animal")

nivel = st.slider("Indica cuál es tu dominio sobre el Mejoramiento Animal (0 = nada, 5 = experto)", 0, 5, 2)

st.image("https://cdn.slidesharecdn.com/ss_thumbnails/mejoramientogeneticoanimal-240418190359-8edceafb-thumbnail.jpg?width=560&fit=bounds")

# Diccionario de razonados por tema (para ejemplo agrego 2 razonados al tema "Dinámica de poblaciones")
temas_razonados = {
    "Dinámica de poblaciones": [
        """**Razonado 1:**  
Se tienen dos rodeos de cría Hereford (A y B) con diferente estructura en edades al parto.  
Tabla de datos:

| Edad al parto | Rodeo A | Rodeo B |
|---------------|---------|---------|
| 3             | 20      | 33      |
| 4             | 20      | 33      |
| 5             | 20      | 33      |
| 6             | 20      |         |
| 7             | 20      |         |
| Total vacas   | 100     | 99      |
| Edad x n      | 500     | 396     |

Incisos:  
- Calcular intervalo generacional (IG) para ambos rodeos.  
- Interpretar diferencias en IG.  
- Evaluar efectos del porcentaje de parición en la selección de vaquillonas.""",

        """**Razonado 2:**  
Un rodeo presenta una heritabilidad estimada para peso al destete de 0.25. Se dispone de datos de 200 terneros con sus respectivos pesos y registros de sus padres.

Incisos:  
- ¿Cómo influye la heritabilidad en la respuesta a la selección?  
- Diseñar un esquema básico para mejorar peso al destete usando selección directa.""",
        # Puedes agregar hasta 10 razonados por tema...
    ],
    "Factores de corrección": [
        """**Razonado 1:**  
Se requiere corregir el peso de animales por efecto de edad y sexo para compararlos homogéneamente.

Incisos:  
- Explicar la importancia de factores de corrección.  
- Proponer un modelo simple de corrección para el peso."""
    ],
    # Otros temas con listas vacías o con razonados...
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

st.subheader("📘 Haz clic en un tema para ver sus razonados:")

# Lista de temas
temas = list(temas_razonados.keys())

# Mostrar los botones de temas en 2 filas y 6 columnas
cols = st.columns(6)
tema_seleccionado = None
for i, tema in enumerate(temas):
    col = cols[i % 6]
    if col.button(tema, key=f"tema_{i}"):
        tema_seleccionado = tema

# Guardamos la selección en session_state para persistir entre runs
if "tema_seleccionado" not in st.session_state:
    st.session_state.tema_seleccionado = None

if tema_seleccionado:
    st.session_state.tema_seleccionado = tema_seleccionado

if st.session_state.tema_seleccionado:
    st.markdown(f"### 🧠 Razonados de: {st.session_state.tema_seleccionado}")

    razonados = temas_razonados[st.session_state.tema_seleccionado]

    if razonados:
        # Mostrar hasta 10 botones de razonados
        max_razonados = min(10, len(razonados))
        razonado_seleccionado = None

        cols_raz = st.columns(max_razonados)
        for i in range(max_razonados):
            if cols_raz[i].button(f"Razonado {i+1}", key=f"raz_{i}"):
                razonado_seleccionado = i

        # Guardar selección en session_state para persistencia
        if "razonado_seleccionado" not in st.session_state:
            st.session_state.razonado_seleccionado = None

        if razonado_seleccionado is not None:
            st.session_state.razonado_seleccionado = razonado_seleccionado

        # Mostrar el razonado seleccionado (solo texto)
        if st.session_state.razonado_seleccionado is not None:
            st.markdown("---")
            st.markdown(razonados[st.session_state.razonado_seleccionado])
    else:
        st.info("Aún no hay razonados cargados para este tema.")


openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

prompt = st.chat_input("What is up?")
if prompt==None:
   st.stop()

with st.chat_message("user",avatar = "🦖"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.

stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0,
    )
respuesta = stream.choices[0].message.content

with st.chat_message("assistant"):
   st.write(respuesta)

