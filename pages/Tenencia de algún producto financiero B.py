# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:40:52 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['4 productos', 15, '2018'], 
                   ['4 productos', 15, '2021'], 
                   ['Solo 3 productos', 18, '2018'], 
                   ['Solo 3 productos', 19, '2021'], 
                   ['Solo 2 productos', 20, '2018'], 
                   ['Solo 2 productos', 22, '2021'],
                   ['Solo 1 producto', 23, '2018'], 
                   ['Solo 1 producto', 22, '2021'],
                   ['Sin producto', 24, '2018'], 
                   ['Sin producto', 22, '2021']],  
                   columns=['Año', 'Porcentaje', 'Serie'])

chart = alt.Chart(df).mark_bar().encode(
   x=alt.X('Año', axis=alt.Axis(labelAngle=0)),
   xOffset='Serie',
   y=alt.Y('Porcentaje', axis=alt.Axis(grid=False)),
   color='Serie'
).configure_view(
    stroke=None,
)

st.title("Tenencia de algún producto financiero (porcentaje de la población adulta)")
st.subheader("")    
st.subheader("")    
st.header("B) Población según los tipos de productos que ha tenido (2018-2021)") 

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart