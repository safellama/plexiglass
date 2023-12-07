import openai, os

class Model:
    def __init__(self, model_type: str, model_name: str):
        self.model_type = model_type
        self.model_name = model_name

        if self.model_type == 'OpenAI Completion' or self.model_type == 'OpenAI Chat':
            self.model = openai.ChatCompletion
        else:
            raise ValueError("Unsupported model type. We only support openai models for now.")

    def prompt(self, messages: list):
        if self.model_type == 'OpenAI Completion' or self.model_type == 'OpenAI Chat':
            openai.api_key = os.getenv("OPENAI_API_KEY")
            response = self.model.create(model=self.model_name, messages=messages)
            return response['choices'][0]['message']['content']
        else:
            raise ValueError("Unsupported model type. We only support openai models for now.")