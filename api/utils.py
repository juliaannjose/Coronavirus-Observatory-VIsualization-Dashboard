import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import streamlit as st
import time

from src.tasks.inference import inference
from src.analytics.worldmap import (
    confirmed_cases,
    death_cases,
    recovered_cases,
    vaccinated_cases,
)
from src.analytics.graphs import getdata, getstats, plot_rate, min_policy, max_policy


def get_policy_descriptions():
    school_closing_policy = {
        "0": "no measures",
        "1": "recommend closing or all schools open with alterations resulting in significant differences compared to non-Covid-19 operations",
        "2": "require closing (only some levels or categories, eg just high school, or just public schools)",
        "3": "require closing all levels",
    }

    workplace_closing = {
        "0": "no measures",
        "1": "recommend closing (or recommend work from home) or all businesses open with alterations resulting in significant differences compared to non-Covid-19 operation",
        "2": "require closing (or work from home) for some sectors or categories of workers",
        "3": "require closing (or work from home) for all-but-essential workplaces (eg grocery stores, doctors)",
    }
    cancel_events = {
        "0": "no measures",
        "1": "recommend cancelling",
        "2": "require cancelling",
    }

    gatherings_restrictions = {
        "0": "no restrictions",
        "1": "restrictions on very large gatherings (the limit is above 1000 people)",
        "2 ": "restrictions on gatherings between 101-1000 people",
        "3": "restrictions on gatherings between 11-100 people",
        "4": "restrictions on gatherings of 10 people or less }",
    }

    transport_closing = {
        "0": "no measures",
        "1": "recommend closing (or significantly reduce volume/route/means of transport available)",
        "2": "require closing (or prohibit most citizens from using it)",
    }

    stay_home_restrictions = {
        "0": "no measures",
        "1": "recommend not leaving house",
        "2": "require not leaving house with exceptions for daily exercise, grocery shopping, and ‘essential’ trips",
        "3": "require not leaving house with minimal exceptions (eg allowed to leave once a week, or only one person can leave at a time, etc)",
    }

    internal_movement_restrictions = {
        "0": "no measures",
        "1": "recommend not to travel between regions/cities",
        "2": "internal movement restrictions in place",
    }

    international_movement_restrictions = {
        "0": "no restrictions",
        "1": "screening arrivals",
        "2": "quarantine arrivals from some or all regions",
        "3": "ban arrivals from some regions",
        "4": "ban on all regions or total border closure",
    }

    information_campaigns = {
        "0": "no Covid-19 public information campaign",
        "1": "public officials urging caution about Covid-19",
        "2": "coordinated public information campaign (eg across traditional and social media)",
    }

    testing_policy = {
        "0": "no testing policy",
        "1": "only those who both (a) have symptoms AND (b) meet specific criteria (eg key workers, admitted to hospital, came into contact with a known case, returned from overseas)",
        "2": "testing of anyone showing Covid-19 symptoms",
        "3": "open public testing (eg “drive through” testing available to asymptomatic people)",
    }

    contact_tracing = {
        "0": "no contact tracing",
        "1": "limited contact tracing; not done for all cases",
        "2": "comprehensive contact tracing; done for all identified cases",
    }

    facial_coverings = {
        "0": "No policy",
        "1": "Recommended",
        "2": "Required in some specified shared/public spaces outside the home with other people present, or some situations when social distancing not possible",
        "3": "Required in all shared/public spaces outside the home with other people present or all situations when social distancing not possible",
        "4": "Required outside the home at all times regardless of location or presence of other people",
    }

    vaccination_policy = {
        "0": "No availability",
        "1": "Availability for ONE of following: key workers/ clinically vulnerable groups (non elderly) / elderly groups",
        "2": "Availability for TWO of following: key workers/ clinically vulnerable groups (non elderly) / elderly groups",
        "3": "Availability for ALL of following: key workers/ clinically vulnerable groups (non elderly) / elderly groups",
        "4": "Availability for all three plus partial additional availability (select broad groups/ages)",
        "5": "Universal availability",
    }

    elderly_people_protection = {
        "0": "no measures",
        "1": "Recommended isolation, hygiene, and visitor restriction measures in LTCFs and/or elderly people to stay at home",
        "2": "Narrow restrictions for isolation, hygiene in LTCFs, some limitations on external visitors and/or restrictions protecting elderly people at home",
        "3": "Extensive restrictions for isolation and hygiene in LTCFs, all non-essential external visitors prohibited, and/or all elderly people required to stay at home and not leave the home with minimal exceptions, and receive no external visitors",
    }

    return (
        school_closing_policy,
        workplace_closing,
        cancel_events,
        gatherings_restrictions,
        transport_closing,
        stay_home_restrictions,
        internal_movement_restrictions,
        international_movement_restrictions,
        information_campaigns,
        testing_policy,
        contact_tracing,
        facial_coverings,
        vaccination_policy,
        elderly_people_protection,
    )


def list_of_countries():
    _LIST_OF_COUNTRIES = (
        "Choose one",
        "United States",
        "Qatar",
        "India",
        "Mexcio",
        "China",
        "Brazil",
        "Afghanistan",
        "Hong Kong",
        "Laos",
        "Palau",
        "Cape Verde",
        "Ukraine",
        "Russia",
        "Georgia",
        "Maldives",
        "United Kingdom",
        "New Zealand",
        "Sri Lanka",
        "Poland",
        "Mali",
        "Kosovo",
        "Belarus",
        "Ghana",
        "Japan",
        "Kuwait",
        "Zimbabwe",
        "Pakistan",
        "Liberia",
        "Yemen",
        "Bulgaria",
        "Nepal",
        "Liberia",
        "Ecuador",
        "Finland",
        "Egypt",
        "Costa Rica",
        "Denmark",
        "Tanzania",
        "Indonesia",
        "Singapore",
        "France",
        "Israel",
    )
    return _LIST_OF_COUNTRIES


def get_confirmed():
    """
    This function calls the analytics function confirmed_cases()
    which returns a plotly chart which is a world map
    showing the cumulative number of confirmed cases day-by-day.

    Returns
      -------
      fig : plotly.graph_objs._figure.Figure
          an interactive plotly chart
    """
    fig = confirmed_cases()
    return fig


def get_deaths():
    """
    This function calls the analytics function death_cases()
    which returns a plotly chart which is a world map
    showing the cumulative number of deaths day-by-day.

    Returns
      -------
      fig : plotly.graph_objs._figure.Figure
          an interactive plotly chart
    """
    fig = death_cases()
    return fig


def get_recovered():
    """
    This function calls the analytics function recovered_cases()
    which returns a plotly chart which is a world map
    showing the cumulative number of recoveries day-by-day.

    Returns
      -------
      fig : plotly.graph_objs._figure.Figure
          an interactive plotly chart
    """
    fig = recovered_cases()
    return fig


def get_vaccinated():
    """
    This function calls the analytics function vaccinated_cases()
    which returns a plotly chart which is a world map
    showing the cumulative number of vaccinated cases day-by-day.

    Returns
      -------
      fig : plotly.graph_objs._figure.Figure
          an interactive plotly chart
    """
    fig = vaccinated_cases()
    return fig


def progressbar(n):
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(n)
        my_bar.progress(percent_complete + 1)


def get_articles(search_param):
    """
    This function calls the inference api

    Parameters
      ----------
      search_param : dict
          a dict contaning search arguments
          such as query, no_of_results

    Returns
      -------
      postgres_result : list(list)
          a list of lists containing milvus distance, title,
          abstract, authors, url

    """
    results = inference(search_param)
    return results


def get_data():
    return getdata()


def get_stats(df, sm, sy, em, ey, country):
    return getstats(df, sm, sy, em, ey, country)


def get_plot_rate(result):
    return plot_rate(result)


def get_min_policy(df, sm, sy, em, ey, country):
    return min_policy(df, sm, sy, em, ey, country)


def get_max_policy(df, sm, sy, em, ey, country):
    return max_policy(df, sm, sy, em, ey, country)
