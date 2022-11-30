import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd

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

def plot_rate(country):

    # fetch country data

    Y = [43,32,67,12,86,23,31,50]
    X = [1,2,3,4,5,6,7,8]

    arr = np.random.normal(35, 35, size=35)
    #fig, ax = plt.subplots()
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    plt.tight_layout()
    ax1.set_title('Confirmation rate')
    ax2.set_title('Death rate')
    ax3.set_title('Recovery rate')
    ax4.set_title('Vaccination rate')
    ax1.plot(X,Y)
    ax2.plot(X,Y)
    ax3.plot(X,Y)
    ax4.plot(X,Y)
    return fig

def plot_country(country):
        world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
        
        world_fig, ax = plt.subplots(figsize=(12, 6))
        world.plot(color="lightgrey", ax=ax)
        
        # or plot Africa continent
        result, ax2 = plt.subplots(figsize=(12, 6))
        ax2 = world[world.name == country].plot(figsize=(8,8), edgecolor=u'gray', cmap='Pastel1', ax = ax2)
        
        return result