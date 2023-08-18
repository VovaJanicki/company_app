import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("The BestCompany")
content = """Lorem ipsum is unnecessary if you institute the best practices in web design and process. Copy should be 
             done before design aspects of the site because copy takes less time in general. Today, modern brands value 
             minimal text and writers can easily finish faster than their designer counterparts. Block text was 
             prioritized in the past because the medium of information was primarily books, magazines, and newspapers. 
             However, now that content is consumed through digital mediums, websites that do not include adequate and 
             thoughtful whitespace are perceived as dated.
          """
st.write(content)
st.header("Our Team: ")
col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])