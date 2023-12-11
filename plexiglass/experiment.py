from .model import Model
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatLiteLLM
from .LLM.evaluate import measure_toxicity
import sys
import pandas as pd

class Experiment:
    def __init__(self, model_type: str, model_name: str, mode: str = "llm-chat-testing"):
        self.model = Model(model_type, model_name).model
        self.conversation_history = []
        
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

    def _get_multiline(self, prompt: str = "[llm-chat] Human Tester: "):
        first = input(prompt)
        lines = [first]
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        return "\n".join(lines)

    def conversation(self):
        memory = ConversationBufferWindowMemory(k=3, memory_key="history", return_messages=True)
        try:
            while True:
                user_input = self._get_multiline(prompt = "[llm-chat] Human Tester: ")
                response = self._call_chat(self.model, user_input, memory)
                print("[llm-chat] LLM:", response["response"], "\n")
                self.conversation_history.append(response["response"])
        except KeyboardInterrupt:
            print("\nConversation ended.")
            scores = []
            print("\nCalculating results ...")
            for convo in self.conversation_history:
                scores.append(measure_toxicity(convo))
            results = pd.DataFrame(scores)
            results["response"] = self.conversation_history
            # move column to front
            results = results[["response"]+[col for col in results.columns if col != "response"]]
            print(results)
            sys.exit()