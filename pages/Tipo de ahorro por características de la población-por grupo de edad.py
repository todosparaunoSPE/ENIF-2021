# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['18-29 años', 25, 'Ahorro formal'], 
                   ['18-29 años', 67, 'Ahorro informal'], 
                   ['30-44 años', 24, 'Ahorro formal'], 
                   ['30-44 años', 57, 'Ahorro informal'], 
                   ['45-59 años', 17, 'Ahorro formal'], 
                   ['45-59 años', 45, 'Ahorro informal'],
                   ['60 años y más', 15, 'Ahorro formal'], 
                   ['60 años y más', 33, 'Ahorro informal']],
                    
                   columns=['Año', 'Porcentaje', 'Serie'])

chart = alt.Chart(df).mark_bar().encode(
   x=alt.X('Año', axis=alt.Axis(labelAngle=0)),
   xOffset='Serie',
   y=alt.Y('Porcentaje', axis=alt.Axis(grid=False)),
   color='Serie'
).configure_view(
    stroke=None,
)

st.title("Tipo de ahorro por características de la población (2021) (porcentaje de la población adulta)")
 
st.subheader("")    
st.subheader("")    
st.header("A) Por grupo de edad")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart
