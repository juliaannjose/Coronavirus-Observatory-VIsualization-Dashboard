import streamlit as st
from utils import *

st.set_page_config(page_title="COVID", page_icon=":ghost:", layout="wide")


with st.sidebar:
    # defaults to worldmap which is the home page
    worldmap = st.checkbox("World Map", value=True)
    # checkbox - page containing other graphs
    graphs = st.checkbox("Check graphs")
    # checkbox - semantic search engine
    articles = st.checkbox("Articles")


##############################################################################
# HOME PAGE
##############################################################################
if worldmap:
    st.title(
        "Covid World Map: Confirmed Cases, Deaths, Recoveries, and Vaccination Statistics"
    )

    confirmed, deaths, recovered, vaccinated = st.tabs(
        ["Confirmed Cases", "Deaths", "Recovered", "Vaccinated"]
    )

    with confirmed:
        with st.spinner("Loading graphs..."):
            st.plotly_chart(get_confirmed(), use_container_width=True)
    with deaths:
        with st.spinner("Loading graphs..."):
            st.plotly_chart(get_deaths(), use_container_width=True)
    with recovered:
        with st.spinner("Loading graphs..."):
            st.plotly_chart(get_recovered(), use_container_width=True)
    with vaccinated:
        with st.spinner("Loading graphs..."):
            st.plotly_chart(get_vaccinated(), use_container_width=True)


##############################################################################
# OTHER PAGES
##############################################################################
# semantic search engine
if articles:
    query = st.text_input("What are you looking for?")
    if query:
        txt = '<p style="font-style:italic;color:gray;">Showing top 10 related articles</p>'
        st.markdown(txt, unsafe_allow_html=True)
        search_param = {"query": query}  # add a parameter for "no_of_results"
        articles = get_articles(search_param=search_param)
        # progressbar(100)

        for i in articles:
            distance, title, summary, authors, link = i
            st.title(title)
            if not authors:
                st.write("Author Information Not Available")
            else:
                st.write(authors)
            if not summary:
                st.write("Abstract Not Available")
            else:
                st.write(summary)
            if not link:
                st.write("URL Not Available")
            else:
                st.markdown("[Click here to view the paper](%s)" % link)

#
if graphs:
    country = st.selectbox(
        "Which country?", ("Choose one", "USA", "India", "Mexcio", "China")
    )

    if st.button("get results"):
        st.write("You selected:" + country)
        st.pyplot(plot_rate(country))
        st.pyplot(plot_country(country))
