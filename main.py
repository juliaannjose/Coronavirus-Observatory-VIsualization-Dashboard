import streamlit as st 
#import matplotlib.pyplot as plt
from utils import *
from spark_functions import *
import time

st.set_page_config(page_title="COVID", page_icon=":ghost:", layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Hello World, Welcome to our Big Data Project!!</p>', unsafe_allow_html=True)


with st.sidebar:
    graphs = st.checkbox("Check graphs")
    articles = st.checkbox("Articles")
    policies = st.checkbox("Policies")

if articles:
    query = st.text_input("What are you looking for?")
    if query:
        txt = '<p style="font-style:italic;color:gray;">Showing top 10 related articles</p>'
        st.markdown(txt, unsafe_allow_html=True)
        articles = get_articles(query)
        progressbar(0.1)
        for i in articles:
            title,summary,link = i
            st.title(title)   
            st.write(summary)
            st.markdown("[Click here to learn more](%s)" %link) 

if graphs:
    df = getdata()
    country = st.selectbox(
        'Which country?',
        ('Choose one','United States', 'Qatar','India', 'Mexcio', 'China', 'Brazil', 'Afghanistan', 'Hong Kong',
            'Laos', 'Palau', 'Cape Verde', 'Ukraine', 'Russia', 'Georgia', 'Maldives',
            'United Kingdom', 'New Zealand', 'Sri Lanka', 'Poland', 'Mali', 'Kosovo', 'Belarus', 'Ghana', 'Japan',
            'Kuwait', 'Zimbabwe', 'Pakistan', 'Liberia', 'Yemen', 'Bulgaria', 'Nepal', 'Liberia', 'Ecuador',
            'Finland', 'Egypt', 'Costa Rica', 'Denmark', 'Tanzania', 'Indonesia', 'Singapore', 'France', 'Israel'
         ))
                                    



    col1, col2, _,_,_,_ = st.columns(6)
    months = ['0'+str(x) for x in range(1,10)]
    months.append('11')
    months.append('12')
    years = ['2020','2021','2022']
    with col1:
        startMonth = st.selectbox('Start month',(months))
        endMonth = st.selectbox('End month',(months))
    with col2:
        startYear = st.selectbox('Start year',(years))
        endYear = st.selectbox('End year',(years))
    
    if st.button('get results'):
        total, result = getstats(df, startMonth, startYear, endMonth, endYear, country)
        
        st.write("Total deaths in this time period:",total)
        progressbar(0.6)
        plots = plot_rate(result)
        
        st.pyplot(plots)
        
        #st.pyplot(plot_country(country))

if policies:
    df = getdata()
    country = st.selectbox(
        'Which country?',
        ('Choose one','United States', 'India', 'Mexcio', 'China', 'Brazil', 'Afghanistan', 'Hong Kong',
            'Laos', 'Palau', 'Cape Verde', 'Ukraine', 'Russia', 'Georgia', 'Maldives',
            'United Kingdom', 'New Zealand', 'Sri Lanka', 'Poland', 'Mali', 'Kosovo', 'Belarus', 'Ghana', 'Japan',
            'Kuwait', 'Zimbabwe', 'Pakistan', 'Liberia', 'Yemen', 'Bulgaria', 'Nepal', 'Liberia', 'Ecuador',
            'Finland', 'Egypt', 'Costa Rica', 'Denmark', 'Tanzania', 'Indonesia', 'Singapore', 'France', 'Israel'))


    col1, col2, _,_,_,_ = st.columns(6)
    months = ['0'+str(x) for x in range(1,10)]
    months.append('11')
    months.append('12')
    years = ['2020','2021','2022']
    with col1:
        startMonth = st.selectbox('Start month',(months))
        endMonth = st.selectbox('End month',(months))
    with col2:
        startYear = st.selectbox('Start year',(years))
        endYear = st.selectbox('End year',(years))
    
    if st.button('get policies - min cases'):
        policy = get_min_policy(df, startMonth, startYear, endMonth, endYear, country)
        
        st.write("policies in this time period which lead to minimum cases are as follows:",policy)

    if st.button('get policies - max cases'):
        policy = get_max_policy(df, startMonth, startYear, endMonth, endYear, country)
        
        st.write("policies in this time period which lead to maximum cases are as follows:",policy)

    school_closing_policy = {
    "0" : "no measures",
    "1" : "recommend closing or all schools open with alterations resulting in significant differences compared to non-Covid-19 operations",
    "2" : "require closing (only some levels or categories, eg just high school, or just public schools)",
    "3" : "require closing all levels"
    }

    workplace_closing = {
    "0" : "no measures",
    "1" : "recommend closing (or recommend work from home) or all businesses open with alterations resulting in significant differences compared to non-Covid-19 operation",
    "2" : "require closing (or work from home) for some sectors or categories of workers",
    "3" : "require closing (or work from home) for all-but-essential workplaces (eg grocery stores, doctors)"
    }
    cancel_events = {
    "0" : "no measures",
    "1" : "recommend cancelling",
    "2" : "require cancelling"
    }

    gatherings_restrictions = {
    "0" : "no restrictions",
    "1" : "restrictions on very large gatherings (the limit is above 1000 people)",
    "2 ": "restrictions on gatherings between 101-1000 people",
    "3" : "restrictions on gatherings between 11-100 people",
    "4" : "restrictions on gatherings of 10 people or less }"}

    transport_closing = {
    "0" : "no measures",
    "1" : "recommend closing (or significantly reduce volume/route/means of transport available)",
    "2" : "require closing (or prohibit most citizens from using it)"
    }


    stay_home_restrictions = {
    "0" : "no measures",
    "1" : "recommend not leaving house",
    "2" : "require not leaving house with exceptions for daily exercise, grocery shopping, and ‘essential’ trips",
    "3" : "require not leaving house with minimal exceptions (eg allowed to leave once a week, or only one person can leave at a time, etc)"
    }

    internal_movement_restrictions = {
    "0" : "no measures",
    "1" : "recommend not to travel between regions/cities",
    "2" : "internal movement restrictions in place"
    }

    international_movement_restrictions = {
    "0" : "no restrictions",
    "1" : "screening arrivals",
    "2" : "quarantine arrivals from some or all regions",
    "3" : "ban arrivals from some regions",
    "4" : "ban on all regions or total border closure"
    }

    information_campaigns = {
    "0" : "no Covid-19 public information campaign",
    "1" : "public officials urging caution about Covid-19",
    "2" : "coordinated public information campaign (eg across traditional and social media)"
    }

    testing_policy = {
    "0" : "no testing policy",
    "1" : "only those who both (a) have symptoms AND (b) meet specific criteria (eg key workers, admitted to hospital, came into contact with a known case, returned from overseas)",
    "2" : "testing of anyone showing Covid-19 symptoms",
    "3" : "open public testing (eg “drive through” testing available to asymptomatic people)"
    }

    contact_tracing = {
    "0" : "no contact tracing",
    "1" : "limited contact tracing; not done for all cases",
    "2" : "comprehensive contact tracing; done for all identified cases"
    }

    facial_coverings = {
    "0" : "No policy",
    "1" : "Recommended",
    "2" : "Required in some specified shared/public spaces outside the home with other people present, or some situations when social distancing not possible",
    "3" : "Required in all shared/public spaces outside the home with other people present or all situations when social distancing not possible",
    "4" : "Required outside the home at all times regardless of location or presence of other people"
    }

    vaccination_policy = {
    "0" : "No availability",
    "1" : "Availability for ONE of following: key workers/ clinically vulnerable groups (non elderly) / elderly groups",
    "2" : "Availability for TWO of following: key workers/ clinically vulnerable groups (non elderly) / elderly groups",
    "3" : "Availability for ALL of following: key workers/ clinically vulnerable groups (non elderly) / elderly groups",
    "4" : "Availability for all three plus partial additional availability (select broad groups/ages)",
    "5" : "Universal availability"
    }


    elderly_people_protection ={ 
    "0" : "no measures",
    "1" : "Recommended isolation, hygiene, and visitor restriction measures in LTCFs and/or elderly people to stay at home",
    "2" : "Narrow restrictions for isolation, hygiene in LTCFs, some limitations on external visitors and/or restrictions protecting elderly people at home",
    "3" : "Extensive restrictions for isolation and hygiene in LTCFs, all non-essential external visitors prohibited, and/or all elderly people required to stay at home and not leave the home with minimal exceptions, and receive no external visitors"
    }

    st.write("School closing policy description",school_closing_policy)
    st.write("workplace closing  policy description",workplace_closing)
    st.write("cancelled events policy description",cancel_events)
    st.write(" gatherings restrictions policy description",gatherings_restrictions)
    st.write("transport closing policy description",transport_closing)
    st.write("stay home restrictions policy description",stay_home_restrictions)
    st.write("internal movement restrictionspolicy description",internal_movement_restrictions)
    st.write("international movement restrictions policy description",international_movement_restrictions)
    st.write(" information campaigns policy description",information_campaigns)
    st.write("testing policy description",testing_policy)
    st.write("contact tracing policy description",contact_tracing)
    st.write("facial coverings policy description",facial_coverings)
    st.write("vaccination policy description",vaccination_policy)
    st.write("elderly people protection description",elderly_people_protection)

