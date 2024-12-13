from globals.models import MODELS


class LLMApi:

    def __init__(self, task: str, model_name: str):
        self.task = task
        self.model_name = model_name
        self.llm = MODELS.get_model(self.model_name)()
        print(self.llm)

    def predict(self, prompt):
        return self.llm.predict(prompt=prompt)



