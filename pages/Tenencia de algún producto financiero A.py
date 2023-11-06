import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame([['2015', 68, 'Tiene'], 
                   ['2015', 10, 'Tuvo'], 
                   ['2018', 68, 'Tiene'], 
                   ['2018', 8, 'Tuvo'], 
                   ['2021', 68, 'Tiene'], 
                   ['2021', 8, 'Tuvo']], 
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

st.title("Tenencia de algún producto financiero (porcentaje de la población adulta)")
st.subheader("")    
st.subheader("")    
st.header(" A) Población que tiene o ha tenido un producto financiero (2015-2021)")    
    

st.subheader("")    
st.subheader("")    
st.subheader("")    

chart

st.subheader("")    
st.subheader("")  

st.caption("Nota: Población adulta de 70 años y menos. Se consideran personas que tienen o tuvieron al menos uno de los siguientes productos: cuenta, crédito formal o seguro; para Afore, solamente se consideran las personas que tienen a la fecha del levantamiento. Fuente: Cálculos propios con datos de la ENIF.")