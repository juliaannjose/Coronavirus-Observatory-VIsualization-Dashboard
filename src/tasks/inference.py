"""
This module has a function that will perform a vector search against
the milvus vector database and also fetch metadata corresponding to 
the mulvus search results from postgres.

Use this function for inference purposes.  
"""

from postgres.helpers import postgres_fetch_metadata
from milvus.helpers import milvus_query_results


def inference(arguments):
    """
    This function is what will be called at inference
    time. Given a query, it returns search results.

    Parameters
    ----------
    arguments : dict
        a dict contaning search parameters
        {"query":"","no_of_results":"","model_name":""}

    Returns
    -------
    postgres_result : list(list)
        a list of lists containing milvus distance, title,
        abstract, authors, url

    """
    # variables
    _MILVUS_COLLECTION_NAME = _POSTGRES_TABLE_NAME = "covid_search"
    _MILVUS_INDEX_NAME = "Embedding"
    _MILVUS_SEARCH_PARAM = {"metric_type": "IP", "params": {"nprobe": 128}}
    _NLP_MODEL_NAME = (
        arguments["model_name"]
        if "model_name" in arguments
        else "multi-qa-MiniLM-L6-cos-v1"
    )  # this arg is optional and has a default value
    _NO_OF_RESULTS = (
        arguments["no_of_results"] if "no_of_results" in arguments else 10
    )  # this arg is optional and has a default value
    _QUERY = arguments["query"]

    milvus_results = milvus_query_results(
        collection_name=_MILVUS_COLLECTION_NAME,
        index_name=_MILVUS_INDEX_NAME,
        query=_QUERY,
        model_name=_NLP_MODEL_NAME,
        search_params=_MILVUS_SEARCH_PARAM,
        k=_NO_OF_RESULTS,
    )
    postgres_results = postgres_fetch_metadata(
        milvus_results=milvus_results, table_name=_POSTGRES_TABLE_NAME
    )
    return postgres_results
