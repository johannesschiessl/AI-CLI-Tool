import json

from terminal.utils.style_handling import green, red, cyan, purple
from utils.file_handling import find_path_to_data_file

def message_initialize():
    """
	Initializes the message system by reading configuration data from 'config.json' file, and then prints the AI-Assistant version, GPT model, and a list of available commands.
	"""

    USERNAME_FILE_PATH: str = find_path_to_data_file("config.json")

    with open(USERNAME_FILE_PATH, "r") as file:
        config_data: dict = json.load(file)
        version: str = config_data.get("version", "")
        gpt_model: str = config_data.get("model", "")

    print(green(f"AI-Assistant ({version})"))
    print(red(f"\nModel: {purple(gpt_model)}\n"))

    print(f"Type {cyan('/help')} for a list of commands.")
    print(f"Type {cyan('/exit')} to exit the program.\n")

    print(f"Type {cyan('/configure')} to change the model.")
    print(f"Type {cyan('/reset')} to reset the conversation history.")

def message_configure():
    """
    Function to configure and change the current model for the application.
    """
    print(f"\n{red('Available Models:')}")
    print(f"#1     {purple('gpt-4o')}")
    print(f"#2     {purple('gpt-4o-mini')}")

    with open(find_path_to_data_file("config.json"), "r") as file:
        model_data: dict = json.load(file)
        current_model: str = model_data.get("model", "")

    if current_model:
        print(f"\nCurrent model: {purple(current_model)}")

    print("\nType the number of the model you want to use.")
    model_user_input: str = input("#")

    if model_user_input == "1":
        new_model:str = "gpt-4o"
    elif model_user_input == "2":
        new_model:str = "gpt-4o-mini"
    else:
        print(red("\nInvalid model. Set to previous model."))
        new_model: str = current_model


    with open(find_path_to_data_file("config.json"), 'w') as file:
        json.dump({"model": new_model}, file)

    print("\nModel changed to:", purple(new_model))

def message_reset_conversation():
    """
    Resets the conversation history.
    """
    print("\nYour conversation history has been reset.")


def message_help():
    """
	A function to print the available commands for the user.
    """
    
    print("\nAvailable commands:")
    print(f"     {cyan('/imagine')} - Generate an image")
    print(f"     {cyan('/transcribe')} - Transcribe an audio file")
    print(f"     {cyan('/tts')} - Convert text to speech\n")
    print(f"     {cyan('/configure')} - Configure which model to use")
    print(f"     {cyan('/reset')} - Reset the conversation history\n")
    print(f"     {cyan('/help')} - Display the list of commands")
    print(f"     {cyan('/exit')} - Exit the program")





# Error messages:

def error_unknown():
    """
    No parameters and no return type. Prints a message indicating that an unknown error occurred.
    """
    print(red("\nAn unknown error occurred. Please try again."))

def error_invalid_command():
    """
    A function to handle an error for an invalid command.
    """
    print(red(f"\nInvalid command. Use {cyan('/help')} {red('to see available commands.')}"))

def error_openai():
    """
    A function that handles errors that occur with OpenAI.
    """
    print(red("\nAn error occurred with OpenAI. Please try again."))

error_file_not_found = lambda file_path: print(red(f"\nFile not found: {file_path}"))