from openai_local.handler import run
from openai_local.functions.image_generation import generate_image
from openai_local.functions.text_to_speech import text_to_speech
from openai_local.functions.audio_transcription import transcribe_audio

from terminal.components.user_input import get_user_input
from terminal.components.assistant_output import print_assistant_output

from terminal.components.system_messages import *

from utils.file_handling import create_config_file_if_not_exist


def main():
    """
	Main function for handling user input and executing corresponding commands.
    """
    create_config_file_if_not_exist()

    message_initialize()
    conversation_history: list = []

    while True:
        user_input: str = get_user_input()
        if user_input:
            if user_input[0] == "/":
                if user_input.startswith("/imagine "):
                    generate_image(user_input[9:])
                elif user_input.startswith("/transcribe "):
                    transcribe_audio(user_input[12:])
                elif user_input.startswith("/tts "):
                    text_to_speech(user_input[4:])
                elif user_input == "/reset":
                    conversation_history = []
                    message_reset_conversation()
                elif user_input == "/configure":
                    message_configure()
                elif user_input == "/exit":
                    exit()
                elif user_input == "/help":
                    message_help()
                else:
                    error_invalid_command()
            else:
                conversation_history: list = run(user_input, conversation_history)


if __name__ == '__main__':
    main()
