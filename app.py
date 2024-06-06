import streamlit as st
import pandas as pd
import duckdb

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

st.write("hello world!")

tab1, tab2 = st.tabs(["DuckDb", "Autre"])

with tab1:
    st.dataframe(df)
    sql_query = st.text_area(label="Requête SQL")
    result = duckdb.query(sql_query).df()


    # df2 = pd.DataFrame()

    st.dataframe(result)

