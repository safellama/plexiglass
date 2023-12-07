from litellm import completion
import os

supported_list = ["openai"]

class Model:
    def __init__(self, model_type: str, model_name: str):
        if model_type in supported_list:
            self.model_type = model_type
            self.model_name = model_name
        else:
            raise ValueError("Unsupported model type")

    def prompt(self, messages: list):
            response = completion(self.model_name, messages=messages)
            return response