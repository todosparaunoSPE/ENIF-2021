

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['2018', 63, 'Hasta primaria'], 
                   ['2018', 76, 'Hasta secundaria'], 
                   ['2018', 77, 'Hasta media superior'], 
                   ['2018', 92, 'Licenciatura o mayor'], 
                   ['2021', 62, 'Hasta primaria'], 
                   ['2021', 75, 'Hasta secundaria'], 
                   ['2021', 81, 'Hasta media superior'], 
                   ['2021', 93, 'Licenciatura o mayor']], 
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
st.header("B) Por nivel educativo")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart