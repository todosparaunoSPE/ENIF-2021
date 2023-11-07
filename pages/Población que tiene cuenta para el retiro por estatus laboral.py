# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['18-29 años', 41, 'Sin trabajo remunerado'], 
                   ['18-29 años', 10, 'Con trabajo remunuerado'], 
                   ['30-44 años', 57, 'Sin trabjo remunerado'], 
                   ['30-44 años', 25, 'Con trabjo remunerado'],
                   ['45-59 años', 54, 'Sin trabjo remunerado'], 
                   ['45-59 años', 23, 'Con trabjo remunerado'],
                   ['60 años y más', 29, 'Sin trabajo remunerado'], 
                   ['60 años y más', 13, 'Con trabajo remunerado']],
                   columns=['Año', 'Porcentaje', 'Serie'])

chart = alt.Chart(df).mark_bar().encode(
   x=alt.X('Año', axis=alt.Axis(labelAngle=0)),
   xOffset='Serie',
   y=alt.Y('Porcentaje', axis=alt.Axis(grid=False)),
   #color='Serie'
   
   ).configure_mark(
    #opacity=0.2,
    color='rgb(184,151,90)'
   
).configure_view(
    stroke=None,
)

st.title("Población que tiene cuenta para el retiro por estatus laboral (2021)")
 
st.subheader("")    
st.markdown('<div style="text-align: justify;">¿Para tú conocimiento… la población con una edad entre 30 y 44 años tiene cuenta para el retiro y un trabajo remunerado; es la de mayor porcentaje en estos rubros?</div>', unsafe_allow_html=True)  
st.subheader("")
st.markdown('<div style="text-align: justify;">(porcentaje de la población adulta por grupo de edad)</div>', unsafe_allow_html=True)
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart

st.subheader("")    
st.subheader("")   

st.caption("Nota: En panel A, población adulta de 70 años y menos. Fuente: Cálculos propios con datos de la ENIF.")

