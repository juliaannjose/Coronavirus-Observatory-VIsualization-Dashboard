import streamlit as st
from utils import *

st.set_page_config(page_title="COVID", page_icon=":ghost:", layout="wide")


with st.sidebar:
    utility = st.radio(
        "What would you like to do?",
        ("Interactive Map", "World Statistics", "Search Engine"),
    )


##############################################################################
# HOME PAGE
##############################################################################
if utility == "Interactive Map":

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
if utility == "Search Engine":

    query = st.text_input("Search for an article")
    # milvus search limit - 16384
    no_of_results = st.slider(
        "number of search results", min_value=1, max_value=16384, value=10
    )
    if query:
        txt = f'<p style="font-style:italic;color:gray;">Showing top {no_of_results} related articles</p>'
        st.markdown(txt, unsafe_allow_html=True)
        search_param = {
            "query": query,
            "no_of_results": no_of_results,
        }
        with st.spinner("Searching..."):
            articles = get_articles(search_param=search_param)

            for i in articles:
                title, summary, authors, link = i
                if not title:
                    st.write("Title Not Available")
                else:
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
                    st.markdown("[View Paper](%s)" % link)

# graphs on confirmed cases, deaths, recovery and vaccination rates
if utility == "World Statistics":

    df = get_data()
    country = st.selectbox(
        "Which country?",
        ("Choose one", "USA", "India", "Mexcio", "China", "Brazil"),
    )

    col1, col2, _, _, _, _ = st.columns(6)
    months = ["0" + str(x) for x in range(1, 10)]
    months.append("11")
    months.append("12")
    years = ["2020", "2021", "2022"]
    with col1:
        startMonth = st.selectbox("Start month", (months))
        endMonth = st.selectbox("End month", (months))
    with col2:
        startYear = st.selectbox("Start year", (years))
        endYear = st.selectbox("End year", (years))

    if st.button("get results"):
        total, result = get_stats(df, startMonth, startYear, endMonth, endYear, country)

        st.write("Total deaths in this time period:", total)
        progressbar(0.6)
        plots = get_plot_rate(result)

        st.pyplot(plots)

        # st.pyplot(plot_country(country))
