import streamlit as st
import numpy as np
import pandas as pd

st.title("My First Cloud app")
st.write("A simple DataFrame")

df = pd.DataFrame(np.random.randn(10,2),columns=['col1','col2'])
st.dataframe(df)