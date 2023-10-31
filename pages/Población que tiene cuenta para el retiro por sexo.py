# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['Hombre', 31, '2018'], 
                   ['Mujer', 31, '2018'], 
                   ['Hombre', 49, '2021'], 
                   ['Mujer', 49, '2021']], 
                   columns=['Año', 'Porcentaje', 'Serie'])

chart = alt.Chart(df).mark_bar().encode(
   x=alt.X('Año', axis=alt.Axis(labelAngle=0)),
   xOffset='Serie',
   y=alt.Y('Porcentaje', axis=alt.Axis(grid=False)),
   color='Serie'
).configure_view(
    stroke=None,
)

st.title("Población que tiene cuenta para el retiro por sexo (2018-2021)")
 
st.subheader("")    
st.subheader("")    
st.header("(porcentaje de la población adulta)")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart
