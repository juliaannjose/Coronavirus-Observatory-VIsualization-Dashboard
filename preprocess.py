def load_and_preprocess_data(spark, filepath):
    """
    This function loads the dataset into a spark df and
    preprocesses it by removing unwanted columns and
    filters out null title rows.

    Parameters
    ----------
    filepath : string
        path to dataset
    spark: pyspark.sql.context.SQLContext
        the spark SQLContext used to read the csv


    Returns
    -------
    df : pyspark.sql.dataframe.DataFrame
        csv file loaded into a df
    """

    df = spark.read.csv(filepath, header=True, inferSchema=True)
    cols_to_keep = ["title", "abstract", "authors", "url"]
    df = df[[cols_to_keep]]
    # when creating embeddings based on a column, filter out null values
    df = df.filter(df.title.isNotNull())
    print("Created and Preprocessed Dataset Successfully\n")
    return df
