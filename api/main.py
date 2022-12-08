import streamlit as st
from utils import *

st.set_page_config(page_title="COVID", page_icon=":ghost:", layout="wide")

st.markdown(
    """
<style>
.big-font {
    font-size:30px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown('<p class="big-font">Hello World !!</p>', unsafe_allow_html=True)

with st.sidebar:
    graphs = st.checkbox("Check graphs")
    articles = st.checkbox("Articles")

if articles:
    query = st.text_input("What are you looking for?")
    if query:
        txt = '<p style="font-style:italic;color:gray;">Showing top 10 related articles</p>'
        st.markdown(txt, unsafe_allow_html=True)
        articles = get_articles(query)
        progressbar(0.1)
        for i in articles:
            title, summary, link = i
            st.title(title)
            st.write(summary)
            st.markdown("[Click here to learn more](%s)" % link)

if graphs:
    df = get_data()
    country = st.selectbox(
        "Which country?", ("Choose one", "USA", "India", "Mexcio", "China", "Brazil")
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
        total, result = getstats(df, startMonth, startYear, endMonth, endYear, country)

        st.write("Total deaths in this time period:", total)
        progressbar(0.6)
        plots = get_plot_rate(result)

        st.pyplot(plots)

        # st.pyplot(plot_country(country))
