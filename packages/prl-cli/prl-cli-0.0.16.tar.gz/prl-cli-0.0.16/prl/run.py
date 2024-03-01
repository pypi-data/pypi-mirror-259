import json
from datetime import datetime
from io import BytesIO
from typing import Any, Dict

import click
import requests
from gql import gql
from jsonschema import ValidationError, validate

from .auth import get_auth_token
from .exceptions import PrlException
from .util import (
    RUN_SCHEMA_PATH,
    be_host,
    display_error_and_exit,
    fe_host,
    get_client,
    list_test_suites,
    prompt_user_for_suite,
)


@click.group()
def run():
    """
    Commands relating to starting or viewing runs
    """
    pass


def _run(run_config: Dict[Any, Any], suiteid: str, metadata_map=None):
    try:
        with open(RUN_SCHEMA_PATH, "r") as f:
            schema = json.load(f)
            validate(instance=run_config, schema=schema)
    except ValidationError as e:
        raise PrlException(
            f"Config file provided did not conform to JSON schema. Message: {e.message}"
        )

    body = {"test_suite_id": suiteid, "parameters": run_config}
    if metadata_map is not None:
        body["metadata"] = metadata_map

    response = requests.post(
        url=f"{be_host()}/start_run/",
        headers={"Authorization": get_auth_token()},
        json=body,
    )

    if response.status_code == 200:
        run_id = response.json()["run_id"]
        return f"{fe_host()}/results?run_id={run_id}"
    else:
        raise PrlException(
            f"Could not start run. Received error from server: {response.text}"
        )


@click.command()
@click.argument("config-file", type=click.File("r"), required=True)
@click.option("-s", "--suite-id", required=False)
def start(config_file: bool, suite_id: str = None):
    """
    Start a new run of a test suite.

    Optionally, if the test suite was defined with "fixed_output" fields
    and if the --use-fixed-output flag is passed, then it will
    use a fixed set of outputs instead of querying the model under test.
    This is useful to evaluate the performance of the evaluator itself.
    """
    try:
        parameters = json.load(config_file)
    except Exception:
        display_error_and_exit("Config file was not valid JSON")

    if suite_id is None:
        suite_id = prompt_user_for_suite()

    try:
        run_url = _run(parameters, suite_id)
    except PrlException as e:
        display_error_and_exit(e.message)

    click.secho("Successfully started run.", fg="green")
    click.secho(run_url, bold=True)


@click.command()
@click.argument("run-id", type=click.STRING, required=True)
@click.argument("file", type=click.File("wb"), required=True)
def get_csv(run_id, file: BytesIO):
    """
    Get the CSV file with run results for a given run.

    This is equivalent to clicking 'Export to CSV' on the Run Results
    page within the website.

    Pass the path to a file where the CSV file should be downloaded.
    """

    try:
        response = requests.post(
            url=f"{be_host()}/export_results_to_file/?run_id={run_id}",
            headers={"Authorization": get_auth_token()},
        )

        if response.status_code != 200:
            display_error_and_exit("Received Error from PRL Server: " + response.text)

        file.write(response.content)

    except PrlException as e:
        display_error_and_exit(e.message)

    click.secho("Successfully downloaded the result CSV.", fg="green")


@click.command()
@click.option(
    "--show-archived",
    is_flag=True,
    show_default=True,
    default=False,
    help="When enabled, archived runs are displayed in the output",
)
def list_results(show_archived: bool):
    """
    Display a list of run results.
    """
    query = gql(
        f"""
        query MyQuery {{
          runs(archived: {"null" if show_archived else "false"}) {{
            passPercentage
            status
            runId
            textSummary
            timestamp
            archived
            parameters
            testSuite {{
              title
            }}
          }}
        }}
    """
    )
    results = get_client().execute(query)
    click.secho(
        f"{'Title':40} {'Timestamp':24} {'Status':13} {'Pass %':8} {'Archived':9}",
        bold=True,
    )
    for result in results["runs"]:
        # print(zoneinfo.available_timezones())
        localtz = datetime.now().astimezone().tzinfo  # zoneinfo.ZoneInfo("localtime")

        timestamp = datetime.strptime(
            result["timestamp"], "%Y-%m-%dT%H:%M:%S.%f%z"
        ).astimezone(localtz)
        # Print the timestamp in our own arbitrary format
        timestamp_str = datetime.strftime(timestamp, "%Y-%m-%d %H:%M %Z")
        pass_percentage = "N/A" if result['passPercentage'] is None else f"{result['passPercentage'] * 100:.2f}"
        click.secho(
            f"{result['testSuite']['title'][:38]:40} {timestamp_str:24} {result['status']:13} {pass_percentage:8} {'yes' if result['archived'] else 'no':10}",
        )


@click.command()
@click.argument("run-id", type=click.STRING, required=True)
def status(run_id):
    "CLI command to get the current status of a single run (error, in_progress, success)"
    query = gql(
        f"""
        query MyQuery {{
            run(runId: "{run_id.strip()}") {{
                status
            }}
        }}
        """
    )
    results = get_client().execute(query)
    click.echo(results["run"]["status"])


run.add_command(start)
run.add_command(list_results)
run.add_command(get_csv)
run.add_command(status)
