import streamlit as st
import pandas as pd
import plotly.express as plotly
import psycopg2

def get_engine(): 
 return psycopg2.connect(
                  host = "localhost",
                  port = 5432,
                  database = "project phonepe",
                  user = "postgres",
                  password = "63693103k@"
                          
    )

engine = get_engine()
# ------------------------ PAGE SETUP ------------------------ #
st.set_page_config(page_title="📱 PhonePe Data Insights", layout="wide")
st.title("📊 PhonePe Data Insights Dashboard")

# ------------------------ FILTERS ------------------------ #     host="localhost", database="project phonepe", user="postgres", password="63693103k@


engine = psycopg2.connect(
        host="localhost", database="project phonepe", user="postgres", password="63693103k@"
)

