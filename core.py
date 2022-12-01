import pyspark
import pyspark.sql.functions as f
import os

from milvus_helpers import (
    embeddings_generation,
    milvus_collection_creation,
    milvus_insert_into_db,
    milvus_query_results,
)
from preprocess import load_and_preprocess_data
from postgres_helpers import (
    postgres_table_creation,
    postgres_insert_into_table,
    postgres_fetch_metadata,
)

path_to_data = os.getcwd() + "/data/metadata.csv"
nlp_model_name = "multi-qa-MiniLM-L6-cos-v1"
milvus_collection_name = postgres_table_name = "covid_search"
milvus_index_name = "Embedding"
milvus_index_param = {
    "metric_type": "IP",  # IP for inner product and L2 for euclidean
    "index_type": "IVF_SQ8",  # Quantization-based index, IVF_SQ8 - high speed query but minor compormise in recall rate than IVF_PQ
    "params": {"nlist": 1024},  # 4 × sqrt(n), n = entities in a segment
}
milvus_search_param = {"metric_type": "IP", "params": {"nprobe": 32}}
number_of_results = 10
query = "covid face coverings"


def load_data_into_milvus_and_postgres():
    """
    This function loads data into Milvus and
    Postgres. This is the offline part of this
    system
    """
    try:
        df = load_and_preprocess_data(spark=spark, filepath=path_to_data)
        dense_vectors = embeddings_generation(
            spark_context=sc,
            df=df,
            column_name="title",
            model_name=nlp_model_name,
        )
        milvus_collection_creation(
            collection_name=milvus_collection_name,
            index_name=milvus_index_name,
            index_param=milvus_index_param,
        )
        milvus_ids = milvus_insert_into_db(
            collection_name=milvus_collection_name, dense_vectors=dense_vectors
        )
        postgres_table_creation(table_name=postgres_table_name)
        postgres_insert_into_table(
            table_name=postgres_table_name,
            df=df,
            corresponding_milvus_ids=milvus_ids,
        )
    except Exception as e:
        print("Failed to push data into milvus and postgres\n")
        print(e)


def inference(query):
    """
    This function is what will be used at inference
    time. Given a query, it returns search results.

    Parameters
    ----------
    query : string
        query in natural language

    Returns
    -------
    postgres_result : list(list)
        a list of lists containing milvus distance, title,
        abstract, authors, url

    """

    milvus_results = milvus_query_results(
        collection_name=milvus_collection_name,
        index_name=milvus_index_name,
        query=query,
        model_name=nlp_model_name,
        search_params=milvus_search_param,
        k=number_of_results,
    )
    postgres_results = postgres_fetch_metadata(
        milvus_results=milvus_results, table_name=postgres_table_name
    )

    return postgres_results


if __name__ == "__main__":
    conf = pyspark.SparkConf().setAppName("bd_project")
    conf.set("spark.driver.memory", "8g")
    conf.set("spark.worker.timeout", "10000000")
    conf.set("spark.driver.maxResultSize", "0")
    conf.set("spark.executor.memory", "8g")
    sc = pyspark.SparkContext(conf=conf)
    spark = pyspark.SQLContext.getOrCreate(sc)

    load_data_into_milvus_and_postgres()
    print(inference(query))
