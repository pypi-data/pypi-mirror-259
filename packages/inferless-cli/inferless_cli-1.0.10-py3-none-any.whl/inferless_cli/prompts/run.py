import json
import time
import os
import subprocess
import requests
import rich
from ruamel import yaml
from rich.progress import Progress, SpinnerColumn, TextColumn
import typer
from inferless_cli.utils.constants import (
    DEFAULT_RUNTIME_FILE_NAME,
    DEFAULT_YAML_FILE_NAME,
)
from inferless_cli.utils.helpers import (
    build_docker_image,
    create_config_from_json,
    create_docker_file,
    decrypt_tokens,
    delete_files,
    generate_template_model,
    get_inputs_from_input_json,
    is_docker_running,
    is_inferless_yaml_present,
    log_exception,
    read_yaml,
    start_docker_container,
    stop_containers_using_port_8000,
    yaml,
)
from inferless_cli.utils.services import get_volume_info_with_id


def local_run():
    _, _, _, workspace_id, _ = decrypt_tokens()
    is_yaml_present = is_inferless_yaml_present(DEFAULT_YAML_FILE_NAME)
    volume_path = None
    if is_yaml_present:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            task_id = progress.add_task(description="Setting up things...", total=None)
            config = read_yaml(DEFAULT_YAML_FILE_NAME)
            if (
                config
                and "configuration" in config
                and "custom_volume_id" in config["configuration"]
                and config["configuration"]["custom_volume_id"]
            ):
                progress.update(
                    task_id, description="Getting your Volume Mount details..."
                )
                volume_data = find_volume_by_id(
                    workspace_id, config["configuration"]["custom_volume_id"]
                )
                volume_path = volume_data["path"]

            if not is_docker_running():
                rich.print("[red]Docker is not running.[/red]")
                log_exception(f"[red]Docker is not running.[/red]: {workspace_id} ")
                raise typer.Exit(1)

            model_name = config["name"]

            requirements_text = """
    # Thu 30 Nov 2023
    accelerate==0.24.1
    boto3==1.28.1
    diffusers==0.24.0
    entrypoints==0.4
    ftfy==6.1.1
    jmespath==1.0.1
    mediapipe==0.10.1
    numpy==1.24.3
    onnx==1.14.0
    onnxruntime==1.15.1
    opencv-contrib-python==4.8.0.74
    optimum==1.9.1
    pandas==2.0.3
    Pillow==10.0.0
    pydantic==1.10.11
    pytesseract==0.3.10
    python-multipart==0.0.6
    requests==2.31.0
    safetensors==0.4.1
    soundfile==0.12.1
    tensorflow==2.13.0
    torch==2.0.1
    transformers==4.35.2
    xformers==0.0.20
    """

            create_requirements_file(requirements_text)

            api_text = f"""
FROM nvcr.io/nvidia/tritonserver:23.06-py3

RUN apt update && apt -y install libssl-dev tesseract-ocr libtesseract-dev ffmpeg

RUN pip install --upgrade pip

COPY inferless_requirements.txt inferless_requirements.txt

RUN pip install  --no-cache-dir  -r inferless_requirements.txt

COPY . /models/{model_name}/1/

##configpbtxt##
                """

            api_text_template_import = f"""
FROM nvcr.io/nvidia/tritonserver:23.06-py3

##oslibraries##

RUN pip install --upgrade pip
 
##piplibraries##

COPY . /models/{model_name}/1/

##configpbtxt##
"""
            yaml_location = DEFAULT_RUNTIME_FILE_NAME

            if (
                "source_framework_type" in config
                and config["source_framework_type"] == "PYTORCH"
            ):
                progress.update(
                    task_id,
                    description="Generating required files for loading model...",
                )
                inputs = create_config_from_json(config)
                generate_template_model(config)
                if os.path.exists(yaml_location):
                    api_text_template_import = api_text_template_import.replace(
                        "##configpbtxt##", f"COPY config.pbtxt /models/{model_name}"
                    )
                else:
                    api_text = api_text.replace(
                        "##configpbtxt##", f"COPY config.pbtxt /models/{model_name}"
                    )

            else:
                inputs = get_inputs_from_input_json(config)

            sys_packages_string = None
            pip_packages_string = None

            if os.path.exists(yaml_location):
                progress.update(
                    task_id,
                    description="Analysing your runtime config...",
                )
                with open(yaml_location, "r") as yaml_file:
                    yaml_dict = yaml.load(yaml_file)
                    sys_packages_string = ""
                    pip_packages_string = ""
                    if (
                        "system_packages" in yaml_dict["build"]
                        and yaml_dict["build"]["system_packages"] is not None
                    ):
                        sys_packages_string = "RUN apt update && apt -y install "
                        for each in yaml_dict["build"]["system_packages"]:
                            sys_packages_string = sys_packages_string + each + " "
                    if (
                        "python_packages" in yaml_dict["build"]
                        and yaml_dict["build"]["python_packages"] is not None
                    ):
                        pip_packages_string = "RUN pip install "
                        for each in yaml_dict["build"]["python_packages"]:
                            pip_packages_string = pip_packages_string + each + " "

                    api_text_template_import = api_text_template_import.replace(
                        "##oslibraries##", sys_packages_string
                    )
                    api_text_template_import = api_text_template_import.replace(
                        "##piplibraries##", pip_packages_string
                    )
                    create_docker_file(api_text_template_import)
            else:
                create_docker_file(api_text)

            progress.update(
                task_id,
                description="Building the Docker Image (Might take some time. Please wait...)",
            )
            # Build Docker image
            build_docker_image()
            rich.print("[green]Docker Image Successfully Built.[/green]\n")

            progress.update(
                task_id,
                description="Starting the Docker Container...",
            )
            # Start Docker container
            stop_containers_using_port_8000()
            start_docker_container(volume_path=volume_path)
            files_to_delete = ["DockerFile", "config.pbtxt", "model.py"]
            delete_files(files_to_delete)
            progress.remove_task(task_id)

            rich.print("[green]Container started successfully.[/green]\n")
            rich.print(
                "\n[bold][yellow]Note: [/underline][/bold]Container usually takes around 15 to 20 seconds to expose the PORT. cURL command should work after that.\n"
            )
            rich.print("\n[bold][underline]CURL COMMAND[/underline][/bold]\n")
            print_curl_command(model_name, inputs)
            # Copy current directory to container
            # time.sleep(30)
            # progress.update(
            #     task_id,
            #     description="Loading the model...",
            # )
            # load_model_template(model_name)
            # progress.remove_task(task_id)
            # rich.print("[green]Model Loaded..[/green]\n")

            # progress.update(
            #     task_id,
            #     description="Testing the inference call...",
            # )
            # res2 = infer_model(model_name, inputs)

            # rich.print("\n[green]Inference successfull..[/green]")

            # rich.print("\n[bold][underline]INFERENCE OUTPUT[/underline][/bold]\n")
            # rich.print(f"[blue]{res2}[/blue]\n")


def create_requirements_file(requirements_text):
    with open("inferless_requirements.txt", "w") as f:
        f.write(requirements_text)


def load_model_template(model_name):
    try:
        url = f"http://localhost:8000/v2/repository/models/{model_name}/load"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        log_exception(e)


# Function to infer using the specified model and inputs
def infer_model(model_name, inputs):
    try:
        url = f"http://localhost:8000/v2/models/{model_name}/infer"
        headers = {"Content-Type": "application/json"}
        data = json.dumps(inputs)
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        log_exception(e)


def execute_curl(curl_command):
    subprocess.run(curl_command, shell=True)


def find_volume_by_id(workspace_id, volume_id):
    volume = get_volume_info_with_id(workspace_id, volume_id)

    return volume


def print_curl_command(model_name: str, inputs: dict):
    curl_command = f"curl --location 'http://localhost:8000/v2/models/{model_name}/infer' --header 'Content-Type: application/json' --data '{json.dumps(inputs)}'"
    rich.print(f"\n{curl_command}")
    return curl_command
