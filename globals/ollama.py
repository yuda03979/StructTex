import os
import subprocess
import tempfile

import requests
import json


class Ollama:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.models_available = []

    def add_model(self, model_name, model_path):
        try:
            # Create a temporary file for the Modelfile
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as modelfile:
                modelfile.write(f"FROM {model_path}\n")
                modelfile_path = modelfile.name

            # Run the ollama command to create the model
            subprocess.run(
                ["ollama", "create", model_name, "-f", modelfile_path],
                check=True
            )
            print(f"Model '{model_name}' created successfully.")
            self.models_available.append(model_name)

        except subprocess.CalledProcessError as e:
            print(f"Error while creating the model: {e}")

        finally:
            # Ensure the temporary Modelfile is deleted
            if os.path.exists(modelfile_path):
                os.remove(modelfile_path)
                print(f"Temporary Modelfile '{modelfile_path}' deleted.")

    def predict(self, model_name, prompt):
        if not model_name in self.models_available:
            raise ValueError(f"ollama dos not know the model {model_name}. available models: {self.models_available}")
        payload = {
            "model": model_name,
            "prompt": prompt,
            "format": "json",
            "stream": False,
            "verbose": False,
            "options": {
                "seed": 0,
                "temperature": 0
            }
        }

        response = requests.post(self.url, json=payload)

        if response.status_code == 200:
            return 0, response.json()
        else:
            return -1, response


ollama = Ollama()
