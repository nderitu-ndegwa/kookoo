import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.set_page_config(layout="wide")
st.title("Credit Card Fraud Detection and visaulization")

#Exploration function(numerical summary)
def explore(df):
    st.write('data')
    st.write(df)

    #numerical summary
    df_types = pd.DataFrame(df.dtypes, columns=['Data Type'])
    numerical_cols = df_types[~df_types['Data Type'].isin(['object', 'bool'])].index.values

    df_types['Count'] = df.count()
    df_types['Unique Values'] = df.nunique()
    df_types['Min'] = df[numerical_cols].min()
    df_types['Max'] = df[numerical_cols].max()
    df_types['Average'] = df[numerical_cols].mean()
    df_types['Median'] = df[numerical_cols].median()
    df_types['St. Dev.'] = df[numerical_cols].std()  
    
    #st.write('Summary:')
    #st.write(df_types)
    #st.line_chart(df)

    #Using the pandas profiler(Profile Report)
    pr = ProfileReport(df, explorative=True)
    st_profile_report(pr)

@st.cache
def get_df(file):

    # get extension and read file
    extension = file.name.split('.')[1]

    if extension.upper() == 'CSV':
        df = pd.read_csv(file)
    elif extension.upper() == 'XLSX':
        df = pd.read_excel(file, engine='openpyxl')
    elif extension.upper() == 'PICKLE':
        df = pd.read_pickle(file)  
    
    return df

#st.title("Credit Card Fraud Detection and visualization")
file = st.file_uploader("Upload dataset in .csv or .xlsx format", type=['csv', 'xlsx'], key = "1")
st.write(file)

option = st.selectbox(
'Choose pandas profiling mode:',
('Minimal', 'Explorative', 'Default'))

if file is None:
    st.write("Please upload your data from the left panel")

if file is not None:
    df = get_df(file)
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

