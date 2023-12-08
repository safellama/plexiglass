from litellm import completion, ModelResponse, Usage, Choices, Message
from transformers import pipeline

supported_list = ["openai", "hf"]


class Model:
    def __init__(self, model_type: str, model_name: str):
        if model_type in supported_list:
            self.model_type = model_type
            self.model_name = model_name
        if self.model_type == "hf":
            # huggingface model
            self._hf_pipeline = pipeline("text-generation", model=model_name)
        else:
            raise ValueError("Unsupported model type")

    def prompt(self, messages: list):
        # TODO: check multiple messages input
        if self.model_type != "hf":
            response = completion(self.model_name, messages=messages)["choices"][0]["message"]["content"]
        elif self.model_type == "hf":
            response = self._hf_pipeline(messages)[0][0]["generated_text"]
        else:
            raise ValueError("Unsupported model type")
        return response['choices'][0]["message"]["content"]