# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['Hasta primaria', 7, 'Ahorro formal'], 
                   ['Hasta primaria', 38, 'Ahorro informal'], 
                   ['Hasta secundaria', 12, 'Ahorro formal'], 
                   ['Hasta secundaria', 52, 'Ahorro informal'], 
                   ['Hasta media superior', 24, 'Ahorro formal'], 
                   ['Hasta media superior', 59, 'Ahorro informal'],
                   ['Licenciatura y más', 45, 'Ahorro formal'], 
                   ['Licenciatura y más', 62, 'Ahorro informal']],
                    
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

st.title("Tipo de ahorro por características de la población (2021) (porcentaje de la población adulta)")
 
st.subheader("")    
st.subheader("¿Sabías que… la población que más ahorra de manera formal y de manera informal tiene un nivel educativo de licenciatura y más?")    
st.subheader("")
st.header("B) Por nivel educativo")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart

st.subheader("")    
st.subheader("")  
 
st.caption("Nota: Los niveles educativos consideran tener al menos un año de educación en el nivel correspondiente. Fuente: Cálculos propios con datos de la ENIF.")
