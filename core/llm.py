from core.base import Base
from llm_directory.llm_api import LLMApi


def llm_apply(self, params):
    response = self.llm_api.predict(params[-1]["response"])
    case = response[0]
    return case, {"response": response}


class LLM(Base):

    def __init__(self, task: str = "json", model_name: str = "chat_gpt", object_name: str = None):
        super().__init__(func=llm_apply, object_name=object_name)

        self.task = task
        self.llm_api = LLMApi(task, model_name)
        self.next_params_keys = ["response"]
