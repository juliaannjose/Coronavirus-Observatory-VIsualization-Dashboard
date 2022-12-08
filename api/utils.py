import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import streamlit as st
import time

from src.analytics.graphs import getdata, getstats, plot_rate


def progressbar(n):
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(n)
        my_bar.progress(percent_complete + 1)


def get_articles(query):
    result = [
        [
            "Header of the article",
            """ Lorem Ipsum is simply dummy text of the printing '
              and typesetting industry. Lorem Ipsum has been the '
              industry's standard dummy text ever since the 1500s, 
              when an unknown printer took a galley of type and scrambled 
              it to make a type specimen book. It has survived not only five 
              centuries, but also the leap into electronic typesetting, 
              remaining essentially unchanged. It was popularised in the 1960s 
              with the release of Letraset sheets containing Lorem Ipsum passages, 
              and more recently with desktop \
              publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
            "https://www.google.com",
        ],
        [
            "Header of the article",
            """ Lorem Ipsum is simply dummy text of the printing '
              and typesetting industry. Lorem Ipsum has been the '
              industry's standard dummy text ever since the 1500s, 
              when an unknown printer took a galley of type and scrambled 
              it to make a type specimen book. It has survived not only five 
              centuries, but also the leap into electronic typesetting, 
              remaining essentially unchanged. It was popularised in the 1960s 
              with the release of Letraset sheets containing Lorem Ipsum passages, 
              and more recently with desktop \
              publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
            "https://www.google.com",
        ],
        [
            "Header of the article",
            """ Lorem Ipsum is simply dummy text of the printing '
              and typesetting industry. Lorem Ipsum has been the '
              industry's standard dummy text ever since the 1500s, 
              when an unknown printer took a galley of type and scrambled 
              it to make a type specimen book. It has survived not only five 
              centuries, but also the leap into electronic typesetting, 
              remaining essentially unchanged. It was popularised in the 1960s 
              with the release of Letraset sheets containing Lorem Ipsum passages, 
              and more recently with desktop \
              publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
            "https://www.google.com",
        ],
        [
            "Header of the article",
            """ Lorem Ipsum is simply dummy text of the printing '
              and typesetting industry. Lorem Ipsum has been the '
              industry's standard dummy text ever since the 1500s, 
              when an unknown printer took a galley of type and scrambled 
              it to make a type specimen book. It has survived not only five 
              centuries, but also the leap into electronic typesetting, 
              remaining essentially unchanged. It was popularised in the 1960s 
              with the release of Letraset sheets containing Lorem Ipsum passages, 
              and more recently with desktop \
              publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
            "https://www.google.com",
        ],
        [
            "Header of the article",
            """ Lorem Ipsum is simply dummy text of the printing '
              and typesetting industry. Lorem Ipsum has been the '
              industry's standard dummy text ever since the 1500s, 
              when an unknown printer took a galley of type and scrambled 
              it to make a type specimen book. It has survived not only five 
              centuries, but also the leap into electronic typesetting, 
              remaining essentially unchanged. It was popularised in the 1960s 
              with the release of Letraset sheets containing Lorem Ipsum passages, 
              and more recently with desktop \
              publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
            "https://www.google.com",
        ],
    ]
    return result


def get_data():
    return getdata()


def get_stats(df, sm, sy, em, ey, country):
    return getstats(df, sm, sy, em, ey, country)


def get_plot_rate(result):
    return plot_rate(result)
