# app.py
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from datetime import datetime, timedelta

DB_FILE = "detections.db"  # Make sure this matches your subscriber's database file

def get_data():
    conn = sqlite3.connect(DB_FILE)
    query = """
    SELECT 
        timestamp,
        detection_number,
        created_at
    FROM detections 
    ORDER BY timestamp;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def main():
    st.title('Detection System Dashboard')
    
    # Get data
    df = get_data()
    
    # Detections over time
    st.subheader('Detection Timeline')
    fig = px.scatter(df, 
                    x='timestamp', 
                    y='detection_number',
                    title='Detections Timeline')
    st.plotly_chart(fig)
    
    # Show raw data
    st.subheader('Raw Data')
    st.dataframe(df)

if __name__ == "__main__":
    main()