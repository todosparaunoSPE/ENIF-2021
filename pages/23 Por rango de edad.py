# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st


from PIL import Image


st.subheader("Por rango de edad")    
#st.subheader("Diseño Estadístico para tomar una muestra y llevar a cabo la Encuesta Nacional de Inclusión Financiera 2021")    
st.subheader("") 

 
 
st.markdown('<div style="text-align: justify;">•	La población que tiene mayor número de cuentas para el retiro por rango de edad es: 30-39 años, con 8,730,874 personas que representan 49% del total de la población adulta de 18 a 70 años que es:  17,813,764 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La población que tiene menor número de cuentas para el retiro por rango de edad es: más de 70 años, con 842,158 personas que representan 12.7% del total de la población adulta de 18 a 70 años que es:  6,643,628 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La mayor población que nunca ha tenido una cuenta para el retiro es: 18-29 años, con 16,574,780 personas que representan 66.5% del total de la población adulta de 18 a 70 años que es:  24,935,476 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La menor población que nunca ha tenido una cuenta para el retiro es: más de 70 años, con 4,832,200 personas que representan 72.7% del total de la población adulta de 18 a 70 años que es:  6,643,628 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La mayor población de hombres que tiene una cuenta para el retiro es: 40-49 años, con 5,006,799 hombres que representan 61.9% del total de la población adulta de 18 a 70 años que es:  8,093,063 hombres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La menor población de mujeres que tiene una cuenta para el retiro es: más de 70 años, con 230,232 mujeres que representan 6.8% del total de la población adulta de 18 a 70 años que es:  3,399,513 mujeres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La mayor población de mujeres que nunca han tenido una cuenta para el retiro es: 18-29 años, con 9,284,948 mujeres que representan 71.8% del total de la población adulta de 18 a 70 años que es:  12,928,397 mujeres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La menor población de hombres que nunca han tenido una cuenta para el retiro es: más de 70 años, con 1,900,270 hombres que representan 58.6% del total de la población adulta de 18 a 70 años que es:  3,244,115 hombres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La mayor población urbana que tiene una cuenta para el retiro es: 30-39 años, con 6,806,128 personas que representan 60.7% del total de la población adulta de 18 a 70 años que es:  11,217,315 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La menor población rural que tiene una cuenta para el retiro es: más de 70 años, con 220,009 personas que representan 8.4% del total de la población adulta de 18 a 70 años que es:  2,633,098 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La mayor población urbana que nunca han tenido una cuenta para el retiro es: 18-29 años, con 10,017,897 personas que representan 61.1% del total de la población adulta de 18 a 70 años que es:  16,408,483 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La menor población rural que nunca han tenido una cuenta para el retiro es: más de 70 años, con 2,235,166 personas que representan 85.6% del total de la población adulta de 18 a 70 años que es:  2,633,098 personas.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La mayor población urbana de hombres que tiene una cuenta para el retiro es: 40-49 años, con 3,682,101 hombres que representan 70.3% del total de la población adulta de 18 a 70 años que es:  5,238,747 hombres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La menor población urbana de mujeres que tiene una cuenta para el retiro es: más de 70 años, con 169,274 mujeres que representan 8.4% del total de la población adulta de 18 a 70 años que es:  2,007,609 mujeres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La mayor población urbana de mujeres que nunca han tenido una cuenta para el retiro es: 18-29 años, con 5,620,440 mujeres que representan 66.4% del total de la población adulta de 18 a 70 años que es:  8,458,922 mujeres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La menor población urbana de hombres que nunca han tenido una cuenta para el retiro es: más de 70 años, con 970,725 hombres que representan 48.5% del total de la población adulta de 18 a 70 años que es:  2,002,921 hombres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La mayor población rural de hombres que tiene una cuenta para el retiro es: 40-49 años, con 1,324,698 hombres que representan 46.4% del total de la población adulta de 18 a 70 años que es:  2,854,316 hombres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La menor población rural de mujeres que tiene una cuenta para el retiro es: más de 70 años, con 60,958 mujeres que representan 4.4% del total de la población adulta de 18 a 70 años que es:  1,391,904 mujeres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La mayor población rural de mujeres que nunca han tenido una cuenta para el retiro es: 18-29 años, con 3,664,508 mujeres que representan 82% del total de la población adulta de 18 a 70 años que es:  4,469,475 mujeres.</div>', unsafe_allow_html=True)
st.subheader("")
st.markdown('<div style="text-align: justify;">•	La menor población rural de hombres que nunca han tenido una cuenta para el retiro es: más de 70 años, con 929,545 hombres que representan 74.9% del total de la población adulta de 18 a 70 años que es: 1,241,194 hombres.</div>', unsafe_allow_html=True)







