# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['Primaria', 2, '2015'], 
                   ['Primaria', 3, '2018'], 
                   ['Primaria', 3, '2021'], 
                   ['Secundaria', 2, '2015'],
                   ['Secundaria', 3, '2018'], 
                   ['Secundaria', 3, '2021'],
                   ['Nivel medio superior', 3, '2015'], 
                   ['Nivel medio superior', 4, '2018'],
                   ['Nivel medio superior', 5, '2021'],
                   ['Licenciatura o más', 6, '2015'], 
                   ['Licenciatura o más', 6, '2018'],
                   ['Licenciatura o más', 10, '2021']],
                   columns=['Año', 'Porcentaje', 'Serie'])

chart = alt.Chart(df).mark_bar().encode(
   x=alt.X('Año', axis=alt.Axis(labelAngle=0)),
   xOffset='Serie',
   y=alt.Y('Porcentaje', axis=alt.Axis(grid=False)),
   color='Serie'
).configure_view(
    stroke=None,
)

st.title("Aportaciones voluntarias a las Afores")
 
st.subheader("")    
st.subheader("")    
st.header("A) Población que realiza aportaciones voluntarias a su Afore (2015-2021) (porcentaje de la población con Afore)")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    



chart

  
st.subheader("")    
st.subheader("")    

st.caption("Nota: Población adulta de 70 años y menos. En panel A, los niveles educativos consideran tener al menos un año de educación en el nivel correspondiente. Los indicadores de nivel primaria son indicativos. En panel B, Otros incluye “No confía en las Afores”, “Porque ya está jubilado” y “Otro”. Las cifras pueden no coincidir debido al redondeo. Fuente: Cálculos propios con datos de la ENIF.")



