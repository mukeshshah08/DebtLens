import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Debt Analysis Dashboard", layout="wide")
st.title("Global Debt Analysis Dashboard")

DATA_FILE = "processed_debt.csv"

if not os.path.exists(DATA_FILE):
    st.warning(f"{DATA_FILE} not found. Run the notebook to create it.")
else:
    df = pd.read_csv(DATA_FILE)
    years = sorted(df['Year'].unique())
    sel_year = st.sidebar.selectbox("Select Year", years, index=len(years)-1)
    topn = st.sidebar.slider("Top N countries by Debt", 5, 50, 10)
    dfy = df[df['Year']==sel_year]

    st.header(f"Top {topn} countries by External Debt ({sel_year})")
    top = dfy.nlargest(topn, 'Debt_USD')[['Country','Debt_USD','Debt_to_GDP']].reset_index(drop=True)
    st.dataframe(top)

    st.header("Choropleth: Debt to GDP")
    fig = px.choropleth(dfy, locations='CountryCode', color='Debt_to_GDP',
                        hover_name='Country', title=f"Debt-to-GDP ({sel_year})")
    st.plotly_chart(fig, use_container_width=True)

    st.header("Country Time Series")
    country = st.selectbox("Choose country", sorted(df['Country'].unique()), index=list(sorted(df['Country'].unique())).index("India") if "India" in df['Country'].unique() else 0)
    cdf = df[df['Country']==country].sort_values('Year')
    fig2 = px.line(cdf, x='Year', y='Debt_USD', title=f"{country} External Debt Over Time")
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""---

**Notes:** Use the notebook to regenerate `processed_debt.csv` with additional indicators and features.
""")
