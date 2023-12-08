from litellm import completion

supported_list = ["openai"]

class Model:
    def __init__(self, model_type: str, model_name: str):
        if model_type in supported_list:
            self.model_type = model_type
            self.model_name = model_name
        elif model_type == "hf":
             # huggingface model
             pass
        else:
            raise ValueError("Unsupported model type")

    def prompt(self, messages: list):
            if self.model_type != "hf":
                response = completion(self.model_name, messages=messages)
                return response['choices'][0]["message"]["content"]
            else:
               # run_hf_inference()
               pass