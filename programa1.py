# carga la libreria streamlit como "st"
import streamlit as st
# asignar un titulo
st.title("Mi primer app en Streamlit")
# agregar un boton
st.button("click")
# agregar globos
st.balloons()

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)


import datetime
import streamlit as st

d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)

st.image("https://www.campus.uni-konstanz.de/sites/unikn/files/styles/artikel_big/public/field/titelbild/Fruit%20bats%20emerging%20at%20dusk%20in%20Kasanka%20National%20Park-Christian%20Ziegler-Max%20Planck%20Institute%20of%20Animal%20Behavior_0.jpg?itok=Pjmx6ie6", caption="Sunrise by the mountains")
