import streamlit as st
import pandas as pd
import plotly.express as plotly
import psycopg2
from sqlalchemy import create_engine
# ------------------------ DATABASE CONNECTION ------------------------ #
 engine = psycopg2.connect(create_engine("postgresql+psycopg2://postgres:63693103k@@localhost:5432/project phonepe"))
    
# ------------------------ PAGE SETUP ------------------------ #
st.set_page_config(page_title="📱 PhonePe Data Insights", layout="wide")
st.title("📊 PhonePe Data Insights Dashboard")

# ------------------------ FILTERS ------------------------ #     host="localhost", database="project phonepe", user="postgres", password="63693103k@

