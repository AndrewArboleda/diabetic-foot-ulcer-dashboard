
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("Alameda Health Equity Dashboard")
st.markdown("This map shows ZIP-level health equity layers for Diabetes, Obesity, DFUs, Stroke, Disability, and Income.")

# Load and display the saved HTML map
map_path = "../06_Results/alameda_combined_with_legend.html"

with open(map_path, 'r', encoding='utf-8') as f:
    map_html = f.read()

components.html(map_html, height=750, scrolling=False)
