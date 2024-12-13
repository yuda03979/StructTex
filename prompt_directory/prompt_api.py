from prompt_directory.prompts import default_prompt_funcs


class PromptApi:

    def __init__(self, model_name, prompt_func=None):
        self.model_name = model_name
        self.prompt_func = prompt_func
        if prompt_func is None:
            self.prompt_func = default_prompt_funcs[self.model_name]

    def predict(self, free_text, type_name, schema, description):
        return self.prompt_func(free_text=free_text, type_name=type_name, schema=schema, description=description)