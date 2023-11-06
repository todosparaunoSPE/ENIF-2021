# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['2015', 56, 'Rural / Tiene'], 
                   ['2015', 10, 'Rural / Tuvo'], 
                   ['2015', 75, 'Urbano / Tiene'], 
                   ['2015', 8, 'Urbano / Tuvo'], 
                   ['2018', 57, 'Rural / Tiene'], 
                   ['2018', 11, 'Rural / Tuvo'], 
                   ['2018', 74, 'Urbano / Tiene'], 
                   ['2018', 6, 'Urbano / Tuvo'], 
                   ['2021', 56, 'Rural / Tiene'], 
                   ['2021', 13, 'Rural / Tuvo'], 
                   ['2021', 74, 'Urbano / Tiene'], 
                   ['2021', 8, 'Urbano / Tuvo']], 
                   
                  columns=['Año', 'Porcentaje', 'Serie'])

chart = alt.Chart(df).mark_bar().encode(
   x=alt.X('Año', axis=alt.Axis(labelAngle=0)),
   xOffset='Serie',
   y=alt.Y('Porcentaje', axis=alt.Axis(grid=False)),
   #color='Serie'
   
   ).configure_mark(
    #opacity=0.2,
    color='rgb(98,17,50)'
   
).configure_view(
    stroke=None,
)

st.title("Población que tiene o ha tenido un producto financiero por tamaño de localidad (2015-2021)")
 
st.subheader("")    
st.subheader("¿Sabías que…en el año 2021 la población de Rural se ha mantenido ligeramente constante en los años, 2015, 2018 y 2021 en cuanto a tener un producto financiero por tamaño de localidad? De igual forma sucede con la población urbana.")    
st.subheader("")
st.header("(porcentaje de la población adulta)")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    


chart

st.caption("Nota: Población adulta de 70 años y menos. Se consideran personas que tienen o tuvieron al menos uno de los siguientes productos: cuenta formal, crédito formal o seguro; para Afore, solamente se consideran las personas que tienen a la fecha del levantamiento. En panel B, se consideran localidades rurales aquellas con población menor a 15 mil habitantes. Las cifras pueden no coincidir debido al redondeo. Fuente: Cálculos propios con datos de la ENIF.")
