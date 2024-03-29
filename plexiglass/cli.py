import typer
from .experiment import Experiment
from InquirerPy import inquirer
import json, os
from typing import List
from getpass import getpass
from typing_extensions import Annotated

app = typer.Typer()

def _load_options() -> dict:
    """Load available model options from options.json.

    Returns:
        dict: Available model options.
    """
    with open('./plexiglass/config/options.json') as f:
        options_json = json.load(f)
        return options_json

def config_llm(metrics: list) -> Experiment:
    """Configure LLM experiment.

    Args:
        metrics (list): List of metrics to evaluate in the experiment.

    Returns:
        Experiment: Experiment object.
    """
    config = _load_options()

    ## select provider
    provider = inquirer.select(
        message="Select your provider:",
        choices=list(config.keys()),
    ).execute()

    ## select model
    model = inquirer.select(
        message="Select your model:",
        choices=config[provider]["model_list"],
    ).execute()

    ## export api key
    api_key = getpass("Please provide your API key: ")
    os.environ[config[provider]["api_key_var_name"]] = api_key

    typer.echo(f"Selected provider and model: {provider}, {model}")
    return Experiment(model_type=provider, model_name=model, metrics=metrics)

def run_llm(experiment: Experiment) -> None:
    """Execute LLM experiment.

    Args:
        experiment (Experiment): Experiment object.
    """
    experiment.conversation()

@app.command()
def main(mode: Annotated[str, typer.Option(help="Mode to run. Choose from: llm-chat, llm-scan")], 
         metrics: Annotated[List[str], typer.Option(help="Metrics to monitor. Choose from: toxicity")]):
    """
    This application performs different tasks based on the selected mode.
    """
    
    if mode.lower() == "llm-chat":
        experiment = config_llm(metrics)
        run_llm(experiment)
    elif mode.lower() == "llm-scan":
        typer.echo("This mode is not implemented yet.")
    else:
        typer.echo("Invalid mode selected.")