import os
import click
import importlib
import json
import yaml
from cwstorm.version import VERSION
from cwstorm.serializers import default
from cwstorm import validator
from tabulate import tabulate
import textwrap

EXAMPLES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")
EXAMPLE_MODULES_PREFIX = "cwstorm.examples."
GET_JOB_FUNCTION_NAME = "get_job"


EXAMPLE_FILES = os.listdir(EXAMPLES_FOLDER)
MODULE_FILES = [
    file for file in EXAMPLE_FILES if file.endswith(".py") and not file.startswith("__")
]
MODULE_NAMES = [file[:-3] for file in MODULE_FILES]  # Remove the .py extension


def _wrap_text(text, width):
    return "\n".join(textwrap.wrap(text, width=width))


########################### MAIN #################################
@click.group(invoke_without_command=True)
@click.pass_context
@click.option("-v", "--version", is_flag=True, help="Print the version and exit.")
def main(ctx, version):
    """Storm Command-line interface."""
    if not ctx.invoked_subcommand:
        if version:
            click.echo(VERSION)
            ctx.exit()
        click.echo(ctx.get_help())
        ctx.exit()


SERIALIZE_HELP = """The structure of serialized DAG. 

default: is a list of nodes and a list of edges. The edges contain source and target pointers to node labels. This is the simplest and easiest to understand. It is also understood by the UI.
"""

FORMAT_HELP = """The output format. JSON and YAML are implemented. XML is not yet implemented.
"""

EXAMPLE_HELP = """The example job to serialize. The examples are in the storm/examples folder. The examples are python modules that contain a function called get_job that returns a job object.
"""


########################### SERIALIZE #############################
@main.command()
@click.option(
    "-f",
    "--fmt",
    "--format",
    help=FORMAT_HELP,
    default="json",
    type=click.Choice(choices=["json", "pretty", "yaml", "xml"], case_sensitive=False),
)
@click.option(
    "-x",
    "--example",
    help=EXAMPLE_HELP,
    default="simple",
    type=click.Choice(choices=MODULE_NAMES, case_sensitive=True),
)
@click.argument("output", nargs=1, type=click.Path(exists=False, resolve_path=True))
def serialize(fmt, example, output):
    """
    Serialize a job to json or yaml.

    Examples:

    # Output json to a file for visualization.

    storm serialize -f json -x frames ~/Desktop/frames.json

    storm serialize -f json -x ass_comp_light -s fargo ~/Desktop/ass_comp_light.json

    # Output yaml to a file for using the the assex job example.

    storm serialize -f yaml -s storm  -x assex  ~/Desktop/assex.yaml

    # ARGO is not yet implemented

    """

    module_name = EXAMPLE_MODULES_PREFIX + example
    module = importlib.import_module(module_name)
    storm_script = getattr(module, GET_JOB_FUNCTION_NAME)
    job = storm_script()

    serialized = default.serialize(job)

    if fmt == "json":
        with open(output, "w", encoding="utf-8") as fh:
            json.dump(serialized, fh)
    elif fmt == "pretty":
        with open(output, "w", encoding="utf-8") as fh:
            json.dump(serialized, fh, indent=3)
    elif fmt == "yaml":
        with open(output, "w", encoding="utf-8") as fh:
            yaml.dump(serialized, fh)
    elif fmt == "xml":
        raise NotImplementedError("XML serialization not implemented yet.")
    else:
        raise ValueError(f"Unknown format: {fmt}")


# for s in a ss_comp_heavy a ss_comp_light a ss_comp_normal a ss_export frames one_task simple_qt ; do  storm serialize -x $s  /Volumes/xhf/dev/cio/inst_tag_assign/public/graphs/$s.json; done


########################### DESERIALIZER #############################
VALIDATOR_INPUT_HELP = """
    Deserializer input format. The input format is the same as the output format.
"""


@main.command()
@click.argument("infile", nargs=1, type=click.Path(exists=True, resolve_path=True))
def validate(infile):
    """
    Validate a JSON file.

    storm validate /path/to/file.json


    """
    print(f"\nValidating {infile}")
    with open(infile, "r", encoding="utf-8") as fh:
        data = json.load(fh)
        result = validator.validate(data)
    MAX_LINE_LENGTH = 40
    for line in result["job_info"]:
        if len(str(line[1])) > MAX_LINE_LENGTH:
            line[1] = _wrap_text(str(line[1]), MAX_LINE_LENGTH)

    print(f"******** Input counts ********")

    print(tabulate(result["input_info"], headers=["Type", "Count"], tablefmt="grid"))

    print(f"\n******** Deserialized job info ********")

    print(
        tabulate(
            result["job_info"], headers=["Param", "Value", "Valid"], tablefmt="grid"
        )
    )

    # click.echo(result)
