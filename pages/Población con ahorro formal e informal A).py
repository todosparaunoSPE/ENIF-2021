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
   #color='Serie'
   
   
   ).configure_mark(
    #opacity=0.2,
    color='rgb(184,151,90)'
   
   
).configure_view(
    stroke=None,
)

st.title("Población con ahorro formal e informal (porcentaje de la población adulta)")
 
st.subheader("")    
st.markdown('<div style="text-align: justify;">¿Para tú conocimiento que… la población que ahorra de manera formal aumento 1 pp en el año 2021 respecto del año 2018? Y que la población en el año 2021 disminuyó 9 pp respecto del año 2018 en cuanto al ahorro informal.</div>', unsafe_allow_html=True) 
st.subheader("")    
st.markdown('<div style="text-align: justify;">A) Población por tenencia de ahorro (2018-2021)</div>', unsafe_allow_html=True)  
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart

st.subheader("")    
st.subheader("") 

st.caption("Nota: Población adulta de 70 años y menos. En panel A, Los porcentajes no suman 100% ya que se puede tener tanto ahorro formal como informal. Las cifras pueden no coincidir debido al redondeo. Fuente: Cálculos propios con datos de la ENIF.")
