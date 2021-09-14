import time
import pandas as pd 
import streamlit as st 
from pyarrow import csv
import pyarrow.parquet as pq
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
    #download=st.button('Download Profile Report')
    pr.to_file("Analysis.html")
    
#st.cache()
@st.cache(persist=False,
          allow_output_mutation=True,
          suppress_st_warning=True,
          show_spinner= True)
          #ttl = 60)
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
    time.sleep(2)
    file = st.file_uploader("Upload dataset in .csv or .xlsx format", type=['csv', 'xlsx'], key = "1")
    st.write(file)


    if not file:
        st.write("Check that you have uploaded a .csv or .xlsx file to proceed")
        return

    df = get_df(file)
    #data = csv.read_csv(df)
    #st.subheader('Map of the data')
    #st.map(df)
    explore(df)
    
    fraud=df[df.Class==1]
    valid=df[df.Class==0]
    outlier_percentage=(df.Class.value_counts()[1]/df.Class.value_counts()[0])*100
    
    st.write('Fraudulent transactions are: %.3f%%'%outlier_percentage)
    st.write('Fraud Cases: ',len(fraud))
    st.write('Valid Cases: ',len(valid))
    
main()
