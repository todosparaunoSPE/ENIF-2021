# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:56:24 2023

@author: jperezr
"""

import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['No le queda dinero para ahorar', 45, '2018'], 
                   ['No le queda dinero para ahorar', 49, '2021'], 
                   ['No sabe cómo hacerlo', 14, '2018'], 
                   ['No sabe cómo hacerlo', 18, '2021'],
                   ['Desconoce las ventajas', 15, '2018'], 
                   ['Desconoce las ventajas', 12, '2021'],
                   ['Ahorra de otra forma', 10, '2018'], 
                   ['Ahorra de otra forma', 9, '2021'],
                   ['Otros(*)', 6, '2018'],
                   ['Otros(*)', 6, '2021'], 
                   ['No confía', 9, '2018'],
                   ['No confía', 5, '2021']],
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
st.header("B) Razón para no realizar aportaciones voluntarias a su Afore (2018-2021) (porcentaje de la población que no realiza aportaciones)")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart

