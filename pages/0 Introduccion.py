# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st


from PIL import Image

st.title("ENIF-2021")
st.subheader("") 
 
st.subheader("ENCUESTA NACIONAL DE INCLUSIÓN FINANCIERA")    
#st.subheader("Diseño Estadístico para tomar una muestra y llevar a cabo la Encuesta Nacional de Inclusión Financiera 2021")    
st.subheader("") 
st.subheader("Introducción")   

st.subheader("")


st.markdown('<div style="text-align: justify;">Se han tomado los datos del libro de tabulados del ENIF-2021, considerando a la población adulta de 18 a 70 años; por región, si es población rural o urbana y el sexo de las personas; en cuanto si han tenido una cuenta de ahorro para el retiro (AFORE). </div>', unsafe_allow_html=True)  
st.subheader("") 
st.markdown('<div style="text-align: justify;">Se presentan unos resúmenes indicando lo que muestran los gráficos y siguiendo el orden:</div>', unsafe_allow_html=True)  
st.subheader("")
st.markdown('<div style="text-align: justify;">•	Población que posee o tuvo posesión de cuenta de ahorro para el retiro</div>', unsafe_allow_html=True) 
st.subheader("")
st.markdown('<div style="text-align: justify;">•	Por región</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	Por rango de edad</div>', unsafe_allow_html=True)

st.subheader("")    

st.markdown('<div style="text-align: justify;">Del reporte de resultados del ENIF-2021 se consideraron las formas que tiene la población de ahorrar: formal e informal. </div>', unsafe_allow_html=True)
st.subheader("") 
st.markdown('<div style="text-align: justify;">También se consideraron los datos de aportaciones voluntarias a las AFORE.</div>', unsafe_allow_html=True)
st.subheader("") 


st.markdown('<div style="text-align: justify;">Población que posee o tuvo posesión de cuenta de ahorro para el retiro</div>', unsafe_allow_html=True)


  
st.subheader("")    
st.markdown('<div style="text-align: justify;">•	La población que nunca ha tenido una cuenta de ahorro es de 44,743,077 que representa el 53.5% del total de la población adulta de 18 a 70 años que es:  83,684,692 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La población urbana que tiene una cuenta para el retiro es: 25,309,393 personas que representan 46.7% del total de la población adulta de 18 a 70 años que es:  54,213,170 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La población rural que tiene una cuenta para el retiro es: 7,410,908 personas que representan 25.1% del total de la población adulta de 18 a 70 años que es:  29,471,522 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La población urbana de hombres que tiene una cuenta para el retiro es: 14,310,092 personas que representan 55.5% del total de la población adulta de 18 a 70 años que es:  25,803,764 hombres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La población urbana de mujeres que tiene una cuenta para el retiro es: 10,999,301 personas que representan 38.7% del total de la población adulta de 18 a 70 años que es:  28,409,406 mujeres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La población urbana de hombres que nunca ha tenido una cuenta para el retiro es: 9,046,273 personas que representan 35.1% del total de la población adulta de 18 a 70 años que es:  25,803,764 hombres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La población urbana de mujeres que nunca ha tenido una cuenta para el retiro es: 15,188,752 personas que representan 53.5% del total de la población adulta de 18 a 70 años que es:  28,409,406 mujeres.</div>', unsafe_allow_html=True)



st.subheader("")    
st.subheader("")    
data = pd.read_csv("datos.csv") #path folder of the data file


st.write(data) #displays the table of data



st.subheader("")



#image = Image.open('cuestionario.jpg')

#st.image(image, caption='Cuestionario')

st.subheader("")
st.subheader("")







