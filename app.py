
import pandas as pd 
import streamlit as st
import plotly.express as px
st.header('Dashboard de Análise de Veículos')
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Criar Histograma')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    fig = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig, use_container_width=True)
scatter_button = st.button('Criar Gráfico de Dispersão')
if scatter_button:
    st.write('Criando gráfico de dispersão: Preço vs Quilometragem')
    
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    st.plotly_chart(fig_scatter, use_container_width=True)