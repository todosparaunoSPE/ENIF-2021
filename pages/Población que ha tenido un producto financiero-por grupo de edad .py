# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['2021', 77, '60 años y más'], 
                   ['2021', 79, '45-59 años'], 
                   ['2021', 82, '30-44 años'], 
                   ['2021', 72, '18-29 años'], 
                   ['2018', 75, '60 años y más'], 
                   ['2018', 79, '45-59 años'], 
                   ['2018', 81, '30-44 años'], 
                   ['2018', 69, '18-29 años']], 
                   columns=['Año', 'Porcentaje', 'Serie'])

chart = alt.Chart(df).mark_bar().encode(
   x=alt.X('Año', axis=alt.Axis(labelAngle=0)),
   xOffset='Serie',
   y=alt.Y('Porcentaje', axis=alt.Axis(grid=False)),
   color='Serie'
).configure_view(
    stroke=None,
)

st.title("Población que ha tenido un producto financiero (2018-2021) (porcentaje de la población adulta)")
 
st.subheader("")    
st.subheader("")    
st.header("A) Por grupo de edad")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart