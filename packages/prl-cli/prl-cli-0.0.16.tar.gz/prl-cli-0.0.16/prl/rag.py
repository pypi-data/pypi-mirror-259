import json

import click
import pandas as pd
import requests

from .auth import get_auth_token
from .util import be_host, display_error_and_exit


@click.group()
def rag():
    """
    Commands relating to starting rag evaluations.
    """
    pass


@click.command()
@click.argument("file", type=click.STRING, required=True)
def upload(file: str):
    """
    Uploads a CSV file to the server for reranking documents.

    Args:
        file (str): The path to the CSV file. The CSV file should
        have a column named "text" containing the documents to be
        reranked as well as a column named id containing the unique
        identifier for each document.

    Returns:
        str: The file ID that can be used to rerank the documents.
    """

    with open(file, "rb") as f:
        response = requests.post(
            f"{be_host()}/upload_rag_file/",
            files={"file": f},
            headers={"Authorization": get_auth_token()},
        )
        if response.status_code != 200:
            display_error_and_exit(f"Failed to upload file {file}")

    click.secho(
        "Successfully Uploaded RAG. File ID: {}".format(response.json()["file_id"]),
        fg="green",
    )


@click.command()
@click.argument("file_id", type=click.STRING, required=True)
@click.argument("query", type=click.STRING, required=True)
@click.option("--light-ranking", type=click.STRING, default=True)
@click.option("--model", type=click.STRING, default="gpt-3")
def rerank(file_id: str, query: str, light_ranking: bool = True, model: str = "gpt-3"):
    """
    Reranks the documents in the file based on the provided query.

    Args:
        file_id (str): The ID of the file containing the documents to be reranked.
        query (str): The query to be used for reranking.
        light_ranking (bool, optional): Whether to use light ranking. Defaults to True.
        model (str, optional): The model to be used. Defaults to "gpt-3".

    Returns:
        None. Prints a list of scores that match the order of the documents in the file.
    """
    response = requests.get(
        f"{be_host()}/evaluate_rag_ranking/",
        params={
            "file_id": file_id,
            "query": query,
            "light_ranking": light_ranking,
            "model": model,
        },
        headers={"Authorization": get_auth_token()},
    )

    if response.status_code != 200:
        display_error_and_exit(f"Failed to run reranking: {file_id}")

    scores = response.json()
    name = file_id.split("/")[-1]
    file_name = f"rag_scores_{name}.json"
    with open(file_name, "w") as f:
        json.dump(scores, f, indent=4)

    click.secho(
        f"Successfully Ran RAG Rankings. Scores saved to {file_name}.",
        fg="green",
    )


rag.add_command(upload)
rag.add_command(rerank)
