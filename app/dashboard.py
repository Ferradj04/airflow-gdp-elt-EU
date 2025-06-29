import streamlit as st
import pandas as pd
import sqlite3
import altair as alt
import plotly.express


st.set_page_config(page_title="Dashboard ELT", layout="wide")

# Connexion à la base SQLite
conn = sqlite3.connect('../data/db.sqlite3')
df = pd.read_sql("SELECT * FROM clean_data", conn)

# UI - Titre
st.title("📊 Dashboard ELT - Données transformées")

# Filtres dynamiques
with st.sidebar:
    st.header("🔍 Filtres")
    noms = st.multiselect("state_name", options=df['state_name'].unique(), default=df['state_name'].unique())
    min_score = st.slider("Score minimum", min_value=int(df['GDP_mi_eu_2024'].min()), max_value=int(df['GDP_mi_eu_2024'].max()), value=int(df['GDP_mi_eu_2024'].min()))

# Application des filtres
filtered_df = df[(df['state_name'].isin(noms)) & (df['GDP_mi_eu_2024'] >= min_score)]

# Affichage du tableau
st.subheader("📋 Données filtrées")
st.dataframe(filtered_df, use_container_width=True)

# Graphique à barres
st.subheader("📈 Répartition des scores")
bar_chart = alt.Chart(filtered_df).mark_bar().encode(
    x='state_name:N',
    y='GDP_mi_eu_2024:Q',
    tooltip=['state_name', 'GDP_mi_eu_2024']
)

st.altair_chart(bar_chart, use_container_width=True)

# Camembert (optionnel, si plusieurs entrées)
if len(filtered_df) > 1:
    st.subheader("🥧 Score par nom (en %)")
    pie_df = filtered_df.copy()
    pie_df['%'] = pie_df['GDP_mi_eu_2024'] / pie_df['GDP_mi_eu_2024'].sum() * 100
    st.plotly_chart({
        'data': [{
            'labels': pie_df['state_name'],
            'values': pie_df['%'],
            'type': 'pie'
        }],
        'layout': {
            'title': 'Partition de Chaque PIB en UE'
        }
    })
