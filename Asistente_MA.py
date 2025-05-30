import streamlit as st

st.set_page_config(page_title="Asistente de Mejoramiento Genético", layout="centered")

st.title(":blue[Asistente virtual para el curso de Mejoramiento Animal] 🐎 🐂 🐷 🐐 🐑 🐔")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.success(f"Hola, {nombre} 👋, bienvenido al curso de Mejoramiento Animal")

nivel = st.slider("Indica cuál es tu dominio sobre el Mejoramiento Animal (0 = nada, 5 = experto)", 0, 5, 2)

st.image("https://cdn.slidesharecdn.com/ss_thumbnails/mejoramientogeneticoanimal-240418190359-8edceafb-thumbnail.jpg?width=560&fit=bounds")

# Razonados con guía paso a paso (ejemplo)
temas_razonados = {
    "Dinámica de poblaciones": [
        {
            "titulo": "Estructura por edad y selección de vaquillonas",
            "problema": """
Se tienen dos rodeos de cría Hereford (A y B) con diferente estructura en edades al parto. Los terneros machos se venden al destete, recriándose solamente las hembras. Los toros se compran.

| Edad al parto | Rodeo A | Rodeo B |
|---------------|---------|---------|
| 3             | 20      | 33      |
| 4             | 20      | 33      |
| 5             | 20      | 33      |
| 6             | 20      |         |
| 7             | 20      |         |
| Total vacas   | 100     | 99      |
| Edad x n      | 500     | 396     |

Se definen los intervalos generacionales (IG) como:

IG rodeo A = 500 / 100 = 5 años (viejo)  
IG rodeo B = 396 / 99 = 4 años (joven)

Con 66% de parición (33 hembras por rodeo):  
- Vaquillonas necesarias:
  - A = 20 → 60.6 %
  - B = 33 → 100 %

Con 86% de parición (43 hembras por rodeo):  
- A = 20 → 46.5 %
- B = 33 → 76.7 %

En el rodeo A con 86% de parición se logra seleccionar las vaquillonas con mayor peso promedio, porque se reduce el % de selección debido a:  
1. Mayor número de animales disponibles.  
2. Menor número de animales a reponer.
""",
            "preguntas": [
                {
                    "texto": "¿Cómo calculas el intervalo generacional (IG) para cada rodeo y qué significa?",
                    "pista": "Recuerda que IG = suma (edad al parto x número de vacas) / total vacas."
                },
                {
                    "texto": "¿Qué implica un IG más alto o más bajo en el contexto del mejoramiento genético?",
                    "pista": "Piensa en cómo afecta la edad promedio al ciclo reproductivo y la rapidez de cambio genético."
                },
                {
                    "texto": "¿Cómo influye el porcentaje de parición en la selección de vaquillonas necesarias?",
                    "pista": "Considera la relación entre número de hembras paridas y la cantidad que debes seleccionar para reponer."
                },
                {
                    "texto": "¿Por qué el rodeo A con 86% de parición puede lograr una mejor selección a pesar de tener un IG más alto?",
                    "pista": "Observa cómo el porcentaje de selección cambia y cómo esto afecta la calidad genética."
                }
            ]
        }
    ],
    # Puedes agregar más temas y razonados aquí
}

st.subheader("📘 Selecciona un tema para ver sus razonados:")

tema = st.selectbox("Tema", list(temas_razonados.keys()))

if tema:
    razonados = temas_razonados[tema]
    if razonados:
        razonado = razonados[0]  # Tomamos el primer razonado para mostrar
        st.markdown(f"### Problema: {razonado['titulo']}")
        st.markdown(razonado['problema'])
        st.markdown("---")

        # Iterar preguntas para guiar al estudiante
        for i, pregunta in enumerate(razonado["preguntas"], 1):
            st.markdown(f"**Pregunta {i}:** {pregunta['texto']}")
            respuesta = st.text_area(f"Escribe tu respuesta para la pregunta {i}:", key=f"resp{i}")

            if respuesta.strip():
                st.info(f"Pista para esta pregunta: {pregunta['pista']}")
                st.markdown("---")
    else:
        st.info("Aún no hay razonados cargados para este tema.")
