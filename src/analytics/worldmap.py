import pyspark
import plotly.express as px

conf = pyspark.SparkConf()
conf.set("spark.driver.memory", "8g")
conf.set("spark.worker.timeout", "10000000")
conf.set("spark.driver.maxResultSize", "0")
conf.set("spark.executor.memory", "8g")

sc = pyspark.SparkContext(conf=conf)
spark = pyspark.SQLContext.getOrCreate(sc)


def confirmed_cases():
    """
    This function uses the country.csv dataset to
    generate a choropleth map showing the number of
    confirmed cases (cumulative) each day. It also has
    a slider for dates.

    Returns
      -------
      fig : plotly.graph_objs._figure.Figure
          an interactive plotly choropleth map
    """
    # hardcoding path to dataset for now
    PATH_TO_DATA = "./data/raw"
    worldmap_df = spark.read.csv(
        PATH_TO_DATA + "/country.csv", header=True, inferSchema=True
    )
    # we only need the following columns
    cols_to_keep = [
        "date",
        "administrative_area_level_1",
        "confirmed",
    ]
    cols_to_drop = [col for col in worldmap_df.columns if col not in cols_to_keep]
    worldmap_df = worldmap_df.drop(*cols_to_drop)
    worldmap_pd_df = worldmap_df.toPandas()

    # plotly slider widget doesn't allow python "datetime" types
    worldmap_pd_df.date = worldmap_pd_df.date.astype(str)

    fig = px.choropleth(
        data_frame=worldmap_pd_df,
        locations="administrative_area_level_1",
        locationmode="country names",
        color="confirmed",
        color_continuous_scale="Burgyl",
        animation_frame="date",
    )
    return fig


def death_cases():
    """
    This function uses the country.csv dataset to
    generate a choropleth map showing the number of
    deaths (cumulative) each day. It also has
    a slider for dates.

    Returns
      -------
      fig : plotly.graph_objs._figure.Figure
          an interactive plotly choropleth map
    """
    # hardcoding path to dataset for now
    PATH_TO_DATA = "./data/raw"
    worldmap_df = spark.read.csv(
        PATH_TO_DATA + "/country.csv", header=True, inferSchema=True
    )
    # we only need the following columns
    cols_to_keep = [
        "date",
        "administrative_area_level_1",
        "deaths",
    ]
    cols_to_drop = [col for col in worldmap_df.columns if col not in cols_to_keep]
    worldmap_df = worldmap_df.drop(*cols_to_drop)
    worldmap_pd_df = worldmap_df.toPandas()

    # plotly slider widget doesn't allow python "datetime" types
    worldmap_pd_df.date = worldmap_pd_df.date.astype(str)

    fig = px.choropleth(
        data_frame=worldmap_pd_df,
        locations="administrative_area_level_1",
        locationmode="country names",
        color="deaths",
        color_continuous_scale="Burgyl",
        animation_frame="date",
    )
    return fig


def recovered_cases():
    """
    This function uses the country.csv dataset to
    generate a choropleth map showing the number of
    recovered cases (cumulative) each day. It also has
    a slider for dates.

    Returns
      -------
      fig : plotly.graph_objs._figure.Figure
          an interactive plotly choropleth map
    """
    # hardcoding path to dataset for now
    PATH_TO_DATA = "./data/raw"
    worldmap_df = spark.read.csv(
        PATH_TO_DATA + "/country.csv", header=True, inferSchema=True
    )
    # we only need the following columns
    cols_to_keep = [
        "date",
        "administrative_area_level_1",
        "recovered",
    ]
    cols_to_drop = [col for col in worldmap_df.columns if col not in cols_to_keep]
    worldmap_df = worldmap_df.drop(*cols_to_drop)
    worldmap_pd_df = worldmap_df.toPandas()

    # plotly slider widget doesn't allow python "datetime" types
    worldmap_pd_df.date = worldmap_pd_df.date.astype(str)

    fig = px.choropleth(
        data_frame=worldmap_pd_df,
        locations="administrative_area_level_1",
        locationmode="country names",
        color="recovered",
        color_continuous_scale="Burgyl",
        animation_frame="date",
    )
    return fig


def vaccinated_cases():
    """
    This function uses the country.csv dataset to
    generate a choropleth map showing the number of
    veccinated cases (cumulative) each day. It also has
    a slider for dates.

    Returns
      -------
      fig : plotly.graph_objs._figure.Figure
          an interactive plotly choropleth map
    """
    # hardcoding path to dataset for now
    PATH_TO_DATA = "./data/raw"
    worldmap_df = spark.read.csv(
        PATH_TO_DATA + "/country.csv", header=True, inferSchema=True
    )
    # we only need the following columns
    cols_to_keep = [
        "date",
        "administrative_area_level_1",
        "vaccines",
    ]
    cols_to_drop = [col for col in worldmap_df.columns if col not in cols_to_keep]
    worldmap_df = worldmap_df.drop(*cols_to_drop)
    worldmap_pd_df = worldmap_df.toPandas()

    # plotly slider widget doesn't allow python "datetime" types
    worldmap_pd_df.date = worldmap_pd_df.date.astype(str)

    fig = px.choropleth(
        data_frame=worldmap_pd_df,
        locations="administrative_area_level_1",
        locationmode="country names",
        color="vaccines",
        color_continuous_scale="Burgyl",
        animation_frame="date",
    )
    return fig
