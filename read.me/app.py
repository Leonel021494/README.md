<<<<<<< HEAD
import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('C:\\Users\\leo_0\\OneDrive\\Escritorio\\read.me\\vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
=======
import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('C:\\Users\\leo_0\\OneDrive\\Escritorio\\read.me\\vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
>>>>>>> aead9857d8872da5c64f436eeebfcd2cdd527fbc
            st.plotly_chart(fig, use_container_width=True)