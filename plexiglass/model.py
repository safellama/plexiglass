from litellm import completion
from transformers import pipeline

supported_list = ["openai", "hf"]


class Model:
    def __init__(self, model_type: str, model_name: str):
        if model_type in supported_list:
            self.model_type = model_type
            self.model_name = model_name
            if self.model_type == "hf":
                # huggingface model
                self._hf_pipeline = pipeline("text-generation", model=model_name, device_map="auto")
        else:
            raise ValueError("Unsupported model type")

    def prompt(self, messages: list) -> str:
        if self.model_type != "hf":
            response = completion(self.model_name, messages=messages)["choices"][0]["message"]["content"]
        elif self.model_type == "hf":
            user_msg = "\n\n".join([m["content"] for m in messages])
            response = self._hf_pipeline(user_msg)[0]["generated_text"]
        else:
            raise ValueError("Unsupported model type")
        return response
