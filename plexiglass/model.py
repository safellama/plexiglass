from langchain.chat_models import ChatLiteLLM

llm_supported_list = ["openai", "anthropic", "cohere"]
dnn_supported_list = []

# available mode: ["llm-benchmarking", "llm-chat-testing", "dnn-testing"]

class Model:
    """Model class for LangChain.
    """
    def __init__(self, model_type: str, model_name: str):
        ## use litellm chat_model for llm testing
        if model_type in llm_supported_list and model_type not in dnn_supported_list:
            self.model = ChatLiteLLM(model=model_name)
        else:
            raise NotImplementedError("Unsupported model type")
