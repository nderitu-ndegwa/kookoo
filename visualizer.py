import pandas as pd 
import pyarrow as pa
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

@st.cache(ttl=30)
def get_df(file):
    time.sleep(2)
    # get extension and read file
    extension = file.name.split('.')[1]

    if extension.upper() == 'CSV':
        df = pd.read_csv(file)
    elif extension.upper() == 'XLSX':
        df = pd.read_excel(file, engine='openpyxl')
    elif extension.upper() == 'PICKLE':
        df = pd.read_pickle(file)  
    
    return df

def main():
    #st.title("Credit Card Fraud Detection and visualization")

    file = st.file_uploader("Upload dataset in .csv or .xlsx format", type=['csv', 'xlsx'], key = "1")
    st.write(file)


    if not file:
        st.write("Check that you have uploaded a .csv or .xlsx file to proceed")
        return

    df = get_df(file)
    data = pa.read_csv(df, read_options=None, Parse_options=None, convert_options=None, MemoryPool memory_pool=None)
    #st.subheader('Map of the data')
    #st.map(df)
    explore(data)

main()
