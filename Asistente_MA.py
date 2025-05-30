import streamlit as st
from openai import OpenAI
from collections import defaultdict
import matplotlib.pyplot as plt

# Configuración inicial
st.set_page_config(page_title="Asistente de Mejoramiento Genético", layout="centered")
st.title(":blue[Asistente virtual para el curso de Mejoramiento Animal] 🐎 🐂 🐷 🐐 🐑 🐔")

# Estado de sesión para uso
if "usuario_nombre" not in st.session_state:
    st.session_state.usuario_nombre = None
if "tema_seleccionado" not in st.session_state:
    st.session_state.tema_seleccionado = None
if "razonado_seleccionado" not in st.session_state:
    st.session_state.razonado_seleccionado = None

# Simulación de base de datos en memoria
uso_por_mes = defaultdict(int)
uso_por_tema = defaultdict(int)
razonados_con_dificultad = defaultdict(int)

# Función de registro de uso
def registrar_uso(usuario, tema=None, razonado=None):
    from datetime import datetime
    mes = datetime.now().strftime("%Y-%m")
    uso_por_mes[mes] += 1
    if tema:
        uso_por_tema[tema] += 1
    if razonado is not None:
        clave = f"{tema} - Razonado {razonado+1}"
        razonados_con_dificultad[clave] += 1

# Entrada del usuario
nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.session_state.usuario_nombre = nombre
    st.success(f"Hola, {nombre} 👋, bienvenido al curso de Mejoramiento Animal")

nivel = st.slider("Indica tu nivel de dominio (0=nada, 5=experto)", 0, 5, 2)

st.image("https://cdn.slidesharecdn.com/ss_thumbnails/mejoramientogeneticoanimal-240418190359-8edceafb-thumbnail.jpg?width=560&fit=bounds")

# Razonados por tema
temas_razonados = {
    "Dinámica de poblaciones": [
        """**Razonado 1: Estructura por edad y selección de vaquillonas**

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

**Incisos:**
- ¿Cuál es el intervalo generacional de cada rodeo?
- ¿Cuántas vaquillonas se necesitan reponer si la parición es del 66%? ¿Y si es del 86%?
- ¿Cuál rodeo permite una mayor intensidad de selección? ¿Por qué?
"""
    ] + ["**Razonado pendiente de carga**" for _ in range(9)],
}

st.subheader("📘 Haz clic en un tema para ver sus razonados:")

# Botones de temas
temas = list(temas_razonados.keys())
cols = st.columns(6)

for i, tema in enumerate(temas):
    col = cols[i % 6]
    if col.button(tema, key=f"tema_{i}"):
        st.session_state.tema_seleccionado = tema
        st.session_state.razonado_seleccionado = None
        registrar_uso(st.session_state.usuario_nombre, tema=tema)

# Si se seleccionó un tema, mostrar botones de razonados
if st.session_state.tema_seleccionado:
    tema = st.session_state.tema_seleccionado
    st.markdown(f"### 🧠 Tema seleccionado: {tema}")
    st.markdown("Selecciona un razonado:")

    cols_raz = st.columns(5)
    for i in range(10):
        if cols_raz[i % 5].button(f"Razonado {i+1}", key=f"raz_{i}"):
            st.session_state.razonado_seleccionado = i
            registrar_uso(
                st.session_state.usuario_nombre,
                tema=tema,
                razonado=i
            )

# Mostrar el razonado (sin respuestas)
if st.session_state.razonado_seleccionado is not None:
    idx = st.session_state.razonado_seleccionado
    razonados = temas_razonados.get(st.session_state.tema_seleccionado, [])
    if idx < len(razonados):
        razonado_completo = razonados[idx]
        razonado_sin_conclusion = razonado_completo.split("**Conclusión:**")[0]
        st.markdown("### 📄 Enunciado del razonado:")
        st.markdown(razonado_sin_conclusion)
    else:
        st.warning("Este razonado aún no ha sido cargado.")

# Gráficos
st.subheader("📊 Estadísticas de uso de la app")

if uso_por_mes:
    st.markdown("**Usuarios por mes:**")
    fig, ax = plt.subplots()
    ax.bar(uso_por_mes.keys(), uso_por_mes.values(), color='skyblue')
    plt.xticks(rotation=45)
    st.pyplot(fig)

if uso_por_tema:
    st.markdown("**Consultas por tema:**")
    fig2, ax2 = plt.subplots()
    ax2.bar(uso_por_tema.keys(), uso_por_tema.values(), color='lightgreen')
    plt.xticks(rotation=45)
    st.pyplot(fig2)

if razonados_con_dificultad:
    st.markdown("**Razonados más consultados:**")
    fig3, ax3 = plt.subplots()
    claves = list(razonados_con_dificultad.keys())
    valores = list(razonados_con_dificultad.values())
    ax3.bar(claves, valores, color='salmon')
    plt.xticks(rotation=90)
    st.pyplot(fig3)
