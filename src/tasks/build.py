"""
This module has a function that will load your dataset, 
preprocess it, create vector embeddings, create a milvus collection and an index, 
push the vectors into the milvus collection, create a postgres table, 
and store metadata into postgres.

Use this function when you want to "build" and set up the 
backend of your search system.

"""

from typing import Optional, Dict

from src.dataset.helpers import load_dataset, preprocess_dataset
from src.model.helpers import generate_embeddings
from src.milvus.helpers import milvus_collection_creation, milvus_insert_into_db
from src.postgres.helpers import postgres_table_creation, postgres_insert_into_table


def build(arguments, spark_context, spark_sql):
    """
    This function loads data into Milvus and
    Postgres. This is the offline part of this
    search system.

    Parameters
    ----------
    arguments : dict
        a dict contaning build arguments
        {"data_path":"","model_name":""}
    spark_context : pyspark.context.SparkContext
    spark_sql : pyspark.sql.context.SQLContext
        the spark SQLContext used to read the csv

    """

    # variables
    _PATH_TO_DATA = arguments["data_path"]
    _NLP_MODEL_NAME = (
        arguments["model_name"]
        if "model_name" in arguments
        else "multi-qa-MiniLM-L6-cos-v1"
    )  # this arg is optional and has a default value
    _MILVUS_COLLECTION_NAME = _POSTGRES_TABLE_NAME = "covid_search"
    _MILVUS_INDEX_NAME = "Embedding"
    _MILVUS_INDEX_PARAM = {
        "metric_type": "IP",  # IP for inner product and L2 for euclidean
        "index_type": "IVF_SQ8",  # Quantization-based index, IVF_SQ8 - high speed query but minor compormise in recall rate than IVF_PQ
        "params": {"nlist": 4096},  # 4 × sqrt(n), n = entities in a segment
    }

    try:
        df = load_dataset(spark=spark_sql, filepath=_PATH_TO_DATA)
        df = preprocess_dataset(df=df)

        dense_vectors = generate_embeddings(
            spark_context=spark_context,
            df=df,
            column_name="title_and_abstract",
            model_name=_NLP_MODEL_NAME,
        )

        milvus_collection_creation(
            collection_name=_MILVUS_COLLECTION_NAME,
            index_name=_MILVUS_INDEX_NAME,
            index_param=_MILVUS_INDEX_PARAM,
        )
        milvus_ids = milvus_insert_into_db(
            collection_name=_MILVUS_COLLECTION_NAME, dense_vectors=dense_vectors
        )
        postgres_table_creation(table_name=_POSTGRES_TABLE_NAME)
        postgres_insert_into_table(
            table_name=_POSTGRES_TABLE_NAME,
            df=df,
            corresponding_milvus_ids=milvus_ids,
        )
        print("Pushed Data to Milvus and Postgres\n")
    except Exception as e:
        print("Failed to Push Data into Milvus and Postgres\n")
        print(e)
