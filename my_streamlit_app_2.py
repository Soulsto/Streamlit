import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Configuration de la page Streamlit
st.set_page_config(page_title='Analyse de Corrélation et de Distribution', layout='wide')

# Fonction pour charger les données depuis une URL
@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

# URL du fichier CSV
data_url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

# Titre de l'application
st.title('Analyse de Corrélation et de Distribution')

# Charger les données
data = load_data(data_url)

# Afficher les 5 premières lignes du dataframe
st.write("Aperçu des données :")
st.dataframe(data.head())

# Afficher les statistiques descriptives
st.write("Statistiques descriptives :")
st.write(data.describe())

# Sélection des colonnes pour l'analyse
st.sidebar.header('Options d\'analyse')
all_columns = data.columns.tolist()
selected_columns = st.sidebar.multiselect('Sélectionnez les colonnes pour l\'analyse', all_columns, all_columns)

if selected_columns:
    # Graphiques de distribution
    st.header('Graphiques de Distribution')
    for col in selected_columns:
        st.subheader(f'Distribution de {col}')
        fig, ax = plt.subplots()
        sns.histplot(data[col], kde=True, ax=ax)
        st.pyplot(fig)

    # Matrice de corrélation
    st.header('Matrice de Corrélation')
    corr_matrix = data[selected_columns].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)


    # Commentaires sur les résultats
    st.header('Commentaires')
    st.write("Ajoutez vos commentaires et observations sur les résultats des analyses ci-dessus.")
    comments = st.text_area("Vos commentaires")

else:
    st.info("Veuillez sélectionner au moins une colonne pour commencer l'analyse.")

# Footer
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: white;
    color: black;
    text-align: center;
    padding: 10px;
}
</style>
<div class="footer">
    <p>Analyse de Corrélation et de Distribution avec Streamlit</p>
</div>
""", unsafe_allow_html=True)
