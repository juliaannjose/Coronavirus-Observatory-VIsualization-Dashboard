import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import streamlit as st
import time
def progressbar(n):
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(n)
        my_bar.progress(percent_complete + 1)
        
    

def get_articles(query):
    result = [
              ["Header of the article",
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
              "https://www.google.com"],
              ["Header of the article",
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
              "https://www.google.com"],
              ["Header of the article",
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
              "https://www.google.com"],
              ["Header of the article",
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
              "https://www.google.com"],
              ["Header of the article",
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
              "https://www.google.com"]
    ]
    return result

def plot_rate(result):

    # fetch country data

    Y = [43,32,67,12,86,23,31,50]
    X = [1,2,3,4,5,6,7,8]

    arr = np.random.normal(100, 25, size=20)
    #fig, ax = plt.subplots()
    #fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True, figsize=(15, 15))


    ax1.tick_params(labelbottom=True, labelsize=15)

    plt.tight_layout(pad = 5)

    plt.subplot(411)
    ax1.plot(X, Y)
    ax1.set_title('Number of Confirmed cases', color='red')
    ax1.set_ylabel('No. of Cases', fontsize = 15)
    ax1.set_xlabel('Time period', fontsize = 10)
    ax1.tick_params(labelbottom=True, labelsize=11)
    ax1.grid()

    plt.subplot(412)
    ax2.plot(X,Y)
    ax2.set_title('Number of Deaths', color='red')
    ax2.set_ylabel('No. of Deaths', fontsize = 15)
    ax2.set_xlabel('Time period', fontsize = 10)
    ax2.tick_params(labelbottom=True, labelsize=12)

    ax2.grid()

    plt.subplot(413)
    ax3.plot(X,Y)
    ax3.set_title('Number of Recovered', color='red')
    ax3.set_ylabel('No. of Recovered', fontsize = 15)
    ax3.set_xlabel('Time period', fontsize = 10)
    ax3.tick_params(labelbottom=True, labelsize=13)

    ax3.grid()

    plt.subplot(414)
    ax4.plot(X,Y)
    ax4.set_title('Number of Vaccinated', color='red')
    ax4.set_ylabel('No. of Vaccinated', fontsize = 15)
    ax4.set_xlabel('Time Period', fontsize = 10)
    ax4.tick_params(labelbottom=True, labelsize=14)
    ax4.grid()

    #fig.show()
    return fig
