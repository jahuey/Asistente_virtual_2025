import streamlit as st

st.set_page_config(page_title="Asistente de Mejoramiento Genético", layout="centered")

st.title(":blue[Asistente virtual para el curso de Mejoramiento Animal] 🐎 🐂 🐷 🐐 🐑 🐔")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.success(f"Hola, {nombre} 👋, bienvenido al curso de Mejoramiento Animal")

nivel = st.slider("Indica cuál es tu dominio sobre el Mejoramiento Animal (0 = nada, 5 = experto)", 0, 5, 2)

st.image("https://cdn.slidesharecdn.com/ss_thumbnails/mejoramientogeneticoanimal-240418190359-8edceafb-thumbnail.jpg?width=560&fit=bounds")

# Diccionario de razonados (puedes ir llenando por tema)
temas_razonados = {
    "Dinámica de poblaciones": [
        """**Problema resuelto: Estructura por edad y selección de vaquillonas**

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

**IG rodeo A = 500 / 100 = 5 años (viejo)**  
**IG rodeo B = 396 / 99 = 4 años (joven)**

Se definen como intervalos generacionales.

**Con 66% de parición (33 hembras por rodeo):**  
- Vaquillonas necesarias:
  - A = 20 → **60.6 %**
  - B = 33 → **100 %**

**Con 86% de parición (43 hembras por rodeo):**  
- A = 20 → **46.5 %**
- B = 33 → **76.7 %**

**Conclusión:**  
En el rodeo A con 86% de parición se logra seleccionar las vaquillonas con mayor peso promedio, porque se reduce el % de selección debido a:  
1. Mayor número de animales disponibles.  
2. Menor número de animales a reponer.
"""
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

st.subheader("📘 Haz clic en un tema para ver sus razonados:")

# Lista de temas
temas = list(temas_razonados.keys())

# Mostrar los botones en 2 filas y 6 columnas
cols = st.columns(6)  # 6 botones por fila

# Mostrar los botones divididos en columnas
for i, tema in enumerate(temas):
    col = cols[i % 6]
    if col.button(tema, use_container_width=True):
        st.markdown(f"### 🧠 Razonados de: {tema}")
        razonados = temas_razonados[tema]
        if razonados:
            for j, r in enumerate(razonados, 1):
                st.markdown(f"**{j}.** {r}")
        else:
            st.info("Aún no hay razonados cargados para este tema.")
        st.markdown("---")


