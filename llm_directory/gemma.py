from globals.globals import GLOBALS
from globals.ollama import ollama


class Gemma:

    def __init__(self):
        self.model_name = "gemma"
        self.model = ollama.add_model(
            model_name=self.model_name,
            model_path=GLOBALS.gemma_path,
        )

    def predict(self, prompt):
        response = ollama.predict(model_name=self.model_name, prompt=prompt)
        return response
