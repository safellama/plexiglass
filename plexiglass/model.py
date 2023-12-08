from litellm import completion, ModelResponse, Usage, Choices, Message
from transformers import AutoModelForCausalLM, AutoTokenizer

supported_list = ["openai", "hf"]


class Model:
    def __init__(self, model_type: str, model_name: str):
        if model_type in supported_list:
            self.model_type = model_type
            self.model_name = model_name
        if self.model_type == "hf":
            # huggingface model
            self._tokenizer = AutoTokenizer.from_pretrained(model_name)
            self._model = AutoModelForCausalLM.from_pretrained(model_name)
        else:
            raise ValueError("Unsupported model type")

    def prompt(self, messages: list) -> ModelResponse:
        if self.model_type != "hf":
            response = completion(self.model_name, messages=messages)
        elif self.model_type == "hf":

            # Text generation
            input_ids = self._tokenizer.encode(messages[0], return_tensors="pt")
            output = self._model.generate(input_ids)
            generated_text = self._tokenizer.decode(output[0])

            # Usage
            prompt_tokens = len(self._tokenizer.tokenize(messages[0]))
            total_tokens = len(self._tokenizer.tokenize(generated_text))

            response = ModelResponse(model=self.model_name,
                                     usage=Usage(completion_tokens=total_tokens - prompt_tokens,
                                                 prompt_tokens=prompt_tokens,
                                                 total_tokens=total_tokens))
            response.choices = Choices(message=Message(content=generated_text))

        else:
            raise ValueError("Unsupported model type")
        return response
