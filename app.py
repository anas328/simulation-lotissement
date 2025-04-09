import streamlit as st
import pandas as pd

st.title("Simulation de Projet de Lotissement")

surface_totale = st.number_input("Surface totale du terrain (m²)", value=10000, step=100)
pourcentage_vendable = st.slider("Pourcentage de surface vendable (%)", 0, 100, 65)
prix_achat_terrain = st.number_input("Prix d'achat du terrain (€)", value=350000, step=1000)
superficie_par_lot = st.number_input("Superficie moyenne par lot (m²)", value=100, step=10)
prix_vente_par_lot = st.number_input("Prix de vente par lot (€)", value=40000, step=1000)
cout_viabilisation_par_m2 = st.number_input("Coût de viabilisation par m² (€)", value=50, step=1)
frais_etudes = st.number_input("Frais d'études et autorisations (€)", value=50000, step=1000)
frais_acquisition = st.number_input("Frais d'acquisition (€)", value=27850, step=1000)
frais_commercialisation_pourcentage = st.slider("Frais de commercialisation (%)", 0, 10, 3)

surface_vendable = surface_totale * (pourcentage_vendable / 100)
nombre_lots = surface_vendable // superficie_par_lot
revenu_total = nombre_lots * prix_vente_par_lot
cout_viabilisation_total = surface_totale * cout_viabilisation_par_m2
frais_commercialisation = revenu_total * (frais_commercialisation_pourcentage / 100)
cout_total = (prix_achat_terrain + frais_acquisition + cout_viabilisation_total +
              frais_etudes + frais_commercialisation)
benefice_net = revenu_total - cout_total
roi = (benefice_net / cout_total) * 100 if cout_total != 0 else 0

st.subheader("Résultats de la Simulation")
st.write(f"**Surface vendable :** {surface_vendable:.2f} m²")
st.write(f"**Nombre de lots vendables :** {int(nombre_lots)}")
st.write(f"**Revenu total estimé :** {revenu_total:,.2f} €")
st.write(f"**Coût total estimé :** {cout_total:,.2f} €")
st.write(f"**Bénéfice net estimé :** {benefice_net:,.2f} €")
st.write(f"**Retour sur investissement (ROI) :** {roi:.2f} %")

st.subheader("Répartition des Coûts et Revenus")
df = pd.DataFrame({
    'Catégorie': ['Revenu Total', 'Coût Total', 'Bénéfice Net'],
    'Montant (€)': [revenu_total, cout_total, benefice_net]
})
st.bar_chart(df.set_index('Catégorie'))
