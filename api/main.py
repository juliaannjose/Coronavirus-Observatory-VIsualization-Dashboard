import streamlit as st

# import matplotlib.pyplot as plt
from utils import *

st.set_page_config(page_title="COVID", page_icon=":ghost:", layout="wide")

# HEader
# st.subheader("Hi, I am Tanmay Khot")
# st.title("A data title")
# st.write("I am write")
# st.write("[Learn more>](https://www.google.com)")


with st.sidebar:
    graphs = st.checkbox("Check graphs")
    articles = st.checkbox("Articles")

if articles:
    query = st.text_input("What are you looking for?")
    if query:
        txt = '<p style="font-style:italic;color:gray;">Showing top 10 related articles</p>'
        st.markdown(txt, unsafe_allow_html=True)
        search_param = {"query": query}  # add a parameter for "no_of_results"
        articles = get_articles(search_param=search_param)
        # progressbar(100)

        for i in articles:
            print(i)
            distance, title, summary, authors, link = i
            st.title(title)
            st.write(authors)
            st.write(summary)
            st.markdown("[Click here to learn more](%s)" % link)

if graphs:
    country = st.selectbox(
        "Which country?", ("Choose one", "USA", "India", "Mexcio", "China")
    )

    if st.button("get results"):
        st.write("You selected:" + country)
        st.pyplot(plot_rate(country))
        st.pyplot(plot_country(country))
