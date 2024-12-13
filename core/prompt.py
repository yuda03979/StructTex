from core.base import Base
from prompt_directory.prompt_api import PromptApi


def prompt_apply(self, params):
    case = 0
    values = params[-1]
    free_text = values["free_text"]
    type_name = values["type_name"]
    schema = values["schema"]
    description = values["description"]
    return case, {"response": self.prompt_api.predict(free_text, type_name, schema, description)}


class Prompt(Base):

    def __init__(self, model_name, prompt_func=None, object_name=None):
        super().__init__(func=prompt_apply, object_name=object_name)
        self.prompt_api = PromptApi(model_name, prompt_func)

