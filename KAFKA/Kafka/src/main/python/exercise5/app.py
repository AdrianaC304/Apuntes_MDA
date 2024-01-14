# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo
data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randn(10)
})

# Configurar la aplicación Streamlit
st.title('Aplicación Streamlit Simple')
st.write('Esta es una aplicación de ejemplo para Streamlit.')

# Mostrar datos en una tabla
st.subheader('Datos:')
st.write(data)

# Crear un gráfico interactivo
st.subheader('Gráfico interactivo:')
chart_type = st.selectbox('Seleccione el tipo de gráfico:', ['line', 'bar', 'scatter'])
fig, ax = plt.subplots()
if chart_type == 'line':
    ax.plot(data['x'], data['y'])
elif chart_type == 'bar':
    ax.bar(data['x'], data['y'])
elif chart_type == 'scatter':
    ax.scatter(data['x'], data['y'])
st.pyplot(fig)

# Agregar funcionalidad adicional, por ejemplo, un slider para ajustar el tamaño del gráfico
st.subheader('Ajuste del tamaño del gráfico:')
chart_size = st.slider('Seleccione el tamaño del gráfico:', min_value=0.5, max_value=2.0, value=1.0)
fig.set_size_inches(6 * chart_size, 4 * chart_size)
st.pyplot(fig)

# Agregar un widget de texto
st.subheader('Widget de texto:')
user_input = st.text_input('Ingrese su comentario:', 'Escribe algo aquí...')
st.write('Usted escribió:', user_input)
