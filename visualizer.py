import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 

st.title("Credit Card Fraud Detection and visaulization")

uploaded_file = st.file_uploader("choose a file to upload")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)


    #Testing with matplotlib code
    fig, ax = plt.subplots()
    df.hist(
        bins=8,
        column = "Amount",
        grid = True,
        figsize = (10, 10),
        color = "#86bf91",
        zorder = 2,
        rwidth = 1.0,
        ax = ax,
    )

    st.write(fig)