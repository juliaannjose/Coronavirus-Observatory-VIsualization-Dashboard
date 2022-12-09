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
from src.analytics.graphs import getdata, getstats, plot_rate


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
