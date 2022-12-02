"""
Use this module to perform a search against the search system

$ python cli/inference.py --query "effect of face coverings for covid" --no_of_results 5 --model_name "multi-qa-MiniLM-L6-cos-v1"

"""
from src.tasks.inference import inference


def parse_arguments():
    """
    Pass the query (in natural langugae), the number of
    results to display, and the name of the
    NLP model for query embedding generation
    (must be the same as the one used at search system
    build time)

    Returns
    -------
    args : dict
        a dict contaning argument paramters
        {"query":"","no_of_results":"","model_name":""}

    """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True, help=" search query")
    parser.add_argument(
        "--no_of_results",
        type=int,
        default=10,
        help=" number of search results",
    )
    parser.add_argument(
        "--model_name",
        type=str,
        default="multi-qa-MiniLM-L6-cos-v1",
        help=" name of the nlp model you want to use for query embedding",
    )
    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    arguments = parse_arguments()
    print(inference(arguments=arguments))
