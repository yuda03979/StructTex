
from typing import List

from llm_directory.gemma import Gemma
from llm_directory.chatgpt import ChatGPT


class Models:

    def __init__(self):
        self.models = {
            "chat_gpt": ChatGPT,
            "gemma": Gemma
        }

    def get_available_models(self) -> list:
        return list(self.models.keys())

    def get_model(self, model_name):
        if model_name.lower() in self.models.keys():
            return self.models[model_name]
        else:
            raise f"do not support model_name: {model_name}"



MODELS = Models()
