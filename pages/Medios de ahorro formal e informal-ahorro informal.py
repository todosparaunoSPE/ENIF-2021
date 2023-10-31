# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['Guardando dinero en casa', 42, '2018'], 
                   ['Guardando dinero en casa', 37, '2021'], 
                   ['Tandas', 22, '2018'], 
                   ['Tandas', 18, '2021'], 
                   ['Caja del trabajo o de conocidos', 14, '2018'], 
                   ['Caja del trabajo o de conocidos', 12, '2021'],
                   ['Guardando dienro con familiares o conocidos', 11, '2018'], 
                   ['Guardando dienro con familiares o conocidos', 9, '2021'],
                   ['Comprando bienes', 9, '2018'], 
                   ['Comprando bienes', 8, '2021'],
                   ['Prestando dienro', 7, '2018'], 
                   ['Prestando dienro', 5, '2021']],
                   columns=['Año', 'Porcentaje', 'Serie'])

chart = alt.Chart(df).mark_bar().encode(
   x=alt.X('Año', axis=alt.Axis(labelAngle=0)),
   xOffset='Serie',
   y=alt.Y('Porcentaje', axis=alt.Axis(grid=False)),
   color='Serie'
).configure_view(
    stroke=None,
)

st.title("Medios de ahorro formal e informal (2018-2021) (porcentaje de la población adulta)")
 
st.subheader("")    
st.subheader("")    
st.header("B) Ahorro informal")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart