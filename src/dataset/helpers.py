"""
This module has functions to:
1. load a csv file into a pyspark dataframe
2. preprocess a pyspark dataframe 
"""


def load_dataset(spark, filepath):
    """
    This function loads the dataset into a spark df.

    Parameters
    ----------
    spark: pyspark.sql.context.SQLContext
        the spark SQLContext used to read the csv
    filepath : string
        path to dataset

    Returns
    -------
    df : pyspark.sql.dataframe.DataFrame
        csv file loaded into a df

    """
    try:
        df = spark.read.csv(filepath, header=True, inferSchema=True)
        print("Dataset Loaded Successfully\n")
        return df
    except Exception as e:
        print("Unable to Load Dataset\n")
        print(e)


def preprocess_dataset(df):
    """
    This function preprocesses a pyspark dataframe
    by keeping only the required columns and
    filtering out null rows in the column that
    embedding generation is based on.

    Parameters
    ----------
    df : pyspark.sql.dataframe.DataFrame
        csv file loaded into a df

    Returns
    -------
    df : pyspark.sql.dataframe.DataFrame
        the preprocessed dataframe
    """
    try:
        cols_to_keep = ["title", "abstract", "authors", "url"]
        df = df[[cols_to_keep]]
        # when creating embeddings based on a column, filter out null values
        embedding_column_name = "title"
        df = df.filter(df[embedding_column_name].isNotNull())
        print("Preprocessed Dataset Successfully\n")
        return df
    except Exception as e:
        print("Preprocessing of Dataset Failed\n")
        print(e)
