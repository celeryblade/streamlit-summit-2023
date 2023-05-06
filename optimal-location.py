import streamlit as st
from snowflake.snowpark import Session

st.title('Optimal store locations based on population')

#=========================================================
# Start Snowflake and load table
#=========================================================

# Establish Snowflake session
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets["snowflake"]).create()

session = create_session()
st.success("Connected to Snowflake!")

# Load data table
@st.cache_data
def load_data(table_name):
    ## Read in data table
    st.write(f"Here's some example data from `{table_name}`:")
    table = session.table(table_name)
    
    ## Do some computation on it
    table = table.limit(100)
    
    ## Collect the results. This will run the query and download the data
    table = table.collect()
    return table

# Select and display data table
table_name = "US_ZIP_CODE_METADATA__POPULATIONS_GEO_CENTROID_LATLNG_CITY_NAMES_STATE_DMA_DEMOGRAPHICS.ZIP_DEMOGRAPHICS.ZIP_CODE_METADATA"

## Display data table
with st.expander("See Table"):
    df = load_data(table_name)
    st.dataframe(df)
