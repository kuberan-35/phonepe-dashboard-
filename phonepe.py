import streamlit as st
import pandas as pd
import plotly.express as plotly
import psycopg2
from sqlalchemy import create_engine
# ------------------------ DATABASE CONNECTION ------------------------ #
def get_engine(): 
         return create_engine("postgresql+psycopg2://postgres:63693103k@@localhost:5432/project phonepe")
engine = get_engine()   
# ------------------------ PAGE SETUP ------------------------ #
st.set_page_config(page_title="📱 PhonePe Data Insights", layout="wide")
st.title("📊 PhonePe Data Insights Dashboard")

# ------------------------ FILTERS ------------------------ #     host="localhost", database="project phonepe", user="postgres", password="63693103k@
@st.cache_data
def get_filter_options():
    df_states = pd.read_sql("SELECT DISTINCT state FROM df_agg_user", engine)
    df_years = pd.read_sql("SELECT DISTINCT year FROM df_agg_user", engine)
    df_years = pd.read_sql("SELECT DISTINCT year FROM df_top_insurance", engine)
    return sorted(df_states['state']), sorted(df_years['year'])

#states, years = get_filter_options()
state_filter = st.sidebar.selectbox("Select State", states)
year_filter = st.sidebar.selectbox("Select Year", years)
