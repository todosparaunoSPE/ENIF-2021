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
   #color='Serie'
   
   
   ).configure_mark(
    #opacity=0.2,
    color='rgb(98,17,50)'
   
   
   
   
).configure_view(
    stroke=None,
)

st.title("Aportaciones voluntarias a las Afores")
 
st.subheader("")    
st.markdown('<div style="text-align: justify;">¿Te informamos que… la razón principal por la cual población no realiza aportaciones voluntarias a su AFORE es: no le queda dinero para ahorrar? Aumentó 4 pp de 2018 a 2021</div>', unsafe_allow_html=True)  
st.subheader("")
st.markdown('<div style="text-align: justify;">B) Razón para no realizar aportaciones voluntarias a su Afore (2018-2021) (porcentaje de la población que no realiza aportaciones)</div>', unsafe_allow_html=True)
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart

st.subheader("")    
st.subheader("")    

st.caption("Nota: Población adulta de 70 años y menos. En panel A, los niveles educativos consideran tener al menos un año de educación en el nivel correspondiente. Los indicadores de nivel primaria son indicativos. En panel B, Otros incluye “No confía en las Afores”, “Porque ya está jubilado” y “Otro”. Las cifras pueden no coincidir debido al redondeo. Fuente: Cálculos propios con datos de la ENIF.")