from model import Model
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatLiteLLM

class Experiment:
    def __init__(self, model_type: str, model_name: str, mode: str = "llm-chat-testing"):
        self.model = Model(model_type, model_name).model
        
        ## define mode
        if mode == "llm-chat-testing":
            self.conversation()
    
    def _call_chat(self, llm: ChatLiteLLM, input: str, memory: ConversationBufferWindowMemory = None) -> str:
        conversation = ConversationChain(
                    llm=llm,
                    memory=memory
        )
        response = conversation(input)
        return response


    def conversation(self):
        memory = ConversationBufferWindowMemory(k=3, memory_key="history", return_messages=True)
        try:
            while True:
                user_input = input("You: ")
                response = self._call_chat(self.model, user_input, memory)
                print("Bot:", response["response"])
        except KeyboardInterrupt:
            print("\nConversation ended.")