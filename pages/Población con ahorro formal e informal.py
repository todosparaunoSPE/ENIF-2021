# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['2018', 20, 'Ahorro formal'], 
                   ['2018', 63, 'Ahorro informal'], 
                   ['2018', 32, 'Sin ahorro'], 
                   ['2021', 21, 'Ahorro formal'], 
                   ['2021', 54, 'Ahorro informal'], 
                   ['2021', 40, 'Sin ahorro']], 
                    
                   columns=['Año', 'Porcentaje', 'Serie'])

chart = alt.Chart(df).mark_bar().encode(
   x=alt.X('Año', axis=alt.Axis(labelAngle=0)),
   xOffset='Serie',
   y=alt.Y('Porcentaje', axis=alt.Axis(grid=False)),
   color='Serie'
).configure_view(
    stroke=None,
)

st.title("Población con ahorro formal e informal (porcentaje de la población adulta)")
 
st.subheader("")    
st.subheader("")    
st.header("A) Población por tenencia de ahorro (2018-2021)")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart

st.subheader("")    
st.subheader("") 

st.caption("Nota: Población adulta de 70 años y menos. En panel A, Los porcentajes no suman 100% ya que se puede tener tanto ahorro formal como informal. Las cifras pueden no coincidir debido al redondeo. Fuente: Cálculos propios con datos de la ENIF.")
