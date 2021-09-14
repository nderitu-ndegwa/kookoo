import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout='wide')
st.title("Credit Card Fraud Detection & Visualization")

@st.cache(allow_output_mutation=True)
def load_data(file):
    df = pd.read_csv(file)
    return df

st.sidebar.title("Upload data")    
uploaded_file = st.sidebar.file_uploader("Choose a file")

option = st.selectbox(
    'Choose pandas profiling mode:',
    ('Minimal', 'Explorative', 'Default'))

if uploaded_file is None:
    st.write("Please upload your data from the left panel")

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.write('data')
    st.write(df)
    if option == "Default":
        pr = ProfileReport(df, title="Statistical Profile Report")

    if option == "Minimal":
        st.write('data')
        st.write(df)
        st.write("Selected option: Minimal. Please consider using Explorative if further exploration is required.")
        pr = ProfileReport(df, title="Statistical Profile Report", minimal=True)

    if option == "Explorative":
        st.write('data')
        st.write(df)
        st.write("Selected option: Explorative. This mode might be computationally expensive. Please consider using Minimal if you are experiencing poor service quality.")
        pr = ProfileReport(df, title="Statistical Profile Report", explorative=True)

    st.title("Statistical Profile Report")
    st_profile_report(pr)
