# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['Ahorro y cheques', 13, '2018'], 
                   ['Ahorro y cheques', 12, '2021'], 
                   ['Nómina', 7, '2018'], 
                   ['Nómina', 10, '2021'], 
                   ['Apoyo de gobierno y otras', 2, '2018'], 
                   ['Apoyo de gobierno y otras', 2, '2021'],
                   ['Inversión y depósitos a plazos', 1, '2018'], 
                   ['Inversión y depósitos a plazos', 2, '2021'],
                   ['Monedero electrónico', 0, '2018'], 
                   ['Monedero electrónico', 1, '2021']],
                   
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
st.header("A) Ahorro formal")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart