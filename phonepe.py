import streamlit as st
import pandas as pd
import plotly.express as plotly
import psycopg2

engine = psycopg2.connect(
        dbname="project phonepe",
        user="postgres",
        password="63693103k@",
        host="localhost",
    )

# ------------------------ PAGE SETUP ------------------------ #
st.set_page_config(page_title="📱 PhonePe Data Insights", layout="wide")
st.title("📊 PhonePe Data Insights Dashboard")

# ------------------------ FILTERS ------------------------ #     host="localhost", database="project phonepe", user="postgres", password="63693103k@

