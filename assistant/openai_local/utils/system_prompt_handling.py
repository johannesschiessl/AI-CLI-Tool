import json
from utils.file_handling import find_path_to_data_file
from utils.date_time_handling import get_current_date_time

def generate_system_prompt():
    """
    Generate a system prompt by finding the path to the data file "config.json" and loading the model information from the file. 
    Return a string that includes the model architecture and the current date and time.
    """
    file_path: str = find_path_to_data_file("config.json")

    with open(file_path, "r") as file:
        file_data: dict = json.load(file)
        model: str = file_data.get("model", "")

    return f"You are a helpful assistant, based on the {model} architecture, a large language model trained by OpenAI. Answer briefly and accurately. Knowledge cutoff: 2024-04 - Current date: {get_current_date_time()}"
    