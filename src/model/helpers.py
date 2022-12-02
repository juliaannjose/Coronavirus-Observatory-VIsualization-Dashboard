"""
This module has functions to:
1. load an NLP model and broadcast it on all spark nodes
2. generate embeddings for a pyspark df
"""


def nlp_model_load_and_broadcast(spark_context, model_name):
    """
    This function loads the nlp model and
    broadcasts it on all nodes

    Parameters
    ----------
    model_name : string
        name of the nlp model
        eg: multi-qa-MiniLM-L6-cos-v1, all-mpnet-base-v2

    spark_context : pyspark.context.SparkContext

    Returns
    -------
    bc_model : pyspark.Broadcast
        the broadcasted object
    """

    from sentence_transformers import SentenceTransformer

    # load the model
    model = SentenceTransformer(model_name)
    # broadcast the model
    try:
        bc_model = spark_context.broadcast(model)
        print(f"Broadcasted model successfully. Model summary: {bc_model.value}\n")
        return bc_model
    except Exception as e:
        print("Broadcast unsuccessful\n")
        print(e)


def generate_embeddings(spark_context, df, column_name, model_name):
    """
    This function generates embeddings for a column in the df
    with the help of a pyspark UDF.

    Parameters
    ----------
    df : pyspark.sql.dataframe.DataFrame
        the dataframe
    column_name : string
        the name of the column you want the embeddings for
    broadcasted_model_object_name : string
        name of the broadcasted object

    Returns
    -------
    dense_vectors : list(numpy.ndarray)
        list of dense vectors corresponding to each row in the df
    """
    import time
    import numpy as np
    import pyspark.sql.functions as f
    from pyspark.sql.types import ArrayType, FloatType

    bc_model = nlp_model_load_and_broadcast(spark_context, model_name)

    def get_embeddings(sentence):
        """
        This UDF generates embeddings for a given sentence
        """
        # print("here")
        sentence_embeddings = bc_model.value.encode(sentence)
        return sentence_embeddings.tolist()

    # convert the python fn "get_embeddings(sentence)" to pyspark udf
    emb_udf = f.udf(get_embeddings, ArrayType(FloatType()))
    # use the udf to create embeddings for all the rows in the df
    df_with_embeddings = df.withColumn("embedding", emb_udf(f.col(column_name)))
    # convert the df 'embeddings' column to a python list to be used by milvus later
    # this step takes a while. ~ 47 minutes for 1.06 mil titles.
    # time it to get "speed" of embedding generation
    start_time = time.time()
    embeddings_list = list(
        df_with_embeddings.select("embedding").toPandas()["embedding"]
    )
    end_time = time.time()
    total = end_time - start_time
    print(f"Successfully generated embeddings in {total} seconds\n")

    # converting list of lists to list of np.arrays (aka dense vectors) for milvus
    dense_vectors = list(np.asarray(embeddings_list))
    return dense_vectors
