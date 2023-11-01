# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st


from PIL import Image

st.title("Introducción")
 
st.subheader("")    
st.subheader("Diseño Estadístico para tomar una muestra y llevar a cabo la Encuesta Nacional de Inclusión Financiera 2021")    
    

st.subheader("El diseño de la muestra es:")
st.subheader("•	Probabilístico")
st.subheader("•	Estratificado")
st.subheader("•	Trietapico")
st.subheader("•	Por conglomerados")

st.subheader("")    
st.subheader("Indicadores y desagregaciones")    





  
st.subheader("")    
st.subheader("1)	Tamaño de localidad: localidades de 15 mil y más habitantes, y de menos de 15 mil habitantes.") 
st.subheader("2)	Sexo de la persona encuestada: mujer u hombre")   
st.subheader("3)	Regiones: Noroeste, Noreste, Occidente y Bajío, Ciudad de México, Centro Sur y Oriente, y Sur.")


data = pd.read_csv("datos.csv") #path folder of the data file
st.write(data) #displays the table of data


st.subheader("El tamaño de muestra ajustado: 15,291 viviendas")
st.subheader("")
st.subheader("La distribución de la muestra se realizó dentro de cada entidad federativa, por tamaño de localidad y estrato, de manera proporcional a su tamaño. La selección de muestra se realizó de manera independiente para cada estrato en tres etapas:")

st.subheader("")

st.subheader("1) Selección de UPM")
st.subheader("2) Selección de vivienda")
st.subheader("3) Persona residente de 18 años y más")

st.subheader("")
st.subheader("La muestra recuperada contiene información de 13,554 personas, que representan un universo de 90 millones 328 mil 320 personas adultas.")

st.subheader("")

st.subheader("Cuestionario")

st.subheader("")

image = Image.open('cuestionario.jpg')

st.image(image, caption='Cuestionario')

st.subheader("")
st.subheader("")

st.subheader("Los resultados de la encuesta presentados por la CNBV y el INEGI revelan:")

st.subheader("")

st.subheader("Una encuesta es un procedimiento de investigación cuantitativa en la que el investigador recopila información mediante el cuestionario previamente diseñado, sin modificar el entorno ni el fenómeno donde se recoge la información ya sea para entregarlo en forma de tríptico, gráfica, tabla o escrita.")

st.subheader("")

st.subheader("•	En 2021 56.7 millones de personas con una edad entre 18 y 70 años contaron con al menos un producto financiero formal (cuenta de ahorro, crédito formal, seguro o AFORE).")

st.subheader("")

st.subheader("•	De 2015 a 2021, la población adulta de 18 a 70 años que ha estado incluida financieramente, es decir que tiene o tuvo al menos un producto financiero, tuvo un crecimiento de 6.4 millones de personas.")

st.subheader("")

st.subheader("•	En 2021, el 58 por ciento de la población tuvo al menos un producto financiero formal.")

st.subheader("")

st.subheader("•	El porcentaje de personas adultas que tienen cuenta y crédito creció de 2018 a 2021; mientras que la posesión de seguros y cuenta Afore disminuyó.")

st.subheader("")

st.subheader("•	Solo una de cada diez personas tiene o ha tenido los cuatro tipos de productos financieros, es decir al menos una cuenta, un crédito, un seguro y cuenta Afore.")

st.subheader("")

st.subheader("•	Una de cada cuatro personas adultas realiza pagos a través de medios electrónicos.")

st.subheader("")


st.subheader("Se presentan algunos gráficos que resumen los resultados obtenidos:")





