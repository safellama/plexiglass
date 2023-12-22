from .model import Model
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatLiteLLM
from .core.evaluate import evaluate
import sys
import pandas as pd
from .colors import bcolors

class Experiment:
    def __init__(self, model_type: str, model_name: str, mode: str = "llm-chat", metrics: list = ["toxicity", "pii"]):
        self.model = Model(model_type, model_name).model
        self.conversation_history = []
        self.metrics = metrics
        
        ## define mode
        if mode == "llm-chat":
            self.conversation()
    
    def _call_chat(self, llm: ChatLiteLLM, input: str, memory: ConversationBufferWindowMemory = None) -> str:
        conversation = ConversationChain(
                    llm=llm,
                    memory=memory
        )
        response = conversation(input)
        return response

    def _get_multiline(self, prompt: str = ""):
        first = input(prompt)
        
        # Check if input starts with triple quotes
        if first.startswith('"""'):
            lines = [first[3:]]  # Remove the starting triple quotes
            in_multiline = True
            while in_multiline:
                line = input()
                if line.endswith('"""'):
                    lines.append(line[:-3])  # Remove the ending triple quotes
                    in_multiline = False
                else:
                    lines.append(line)
        else:
            # Single line input
            lines = [first]

        return "\n".join(lines)

    def conversation(self):
        memory = ConversationBufferWindowMemory(k=3, memory_key="history", return_messages=True)
        try:
            while True:
                user_input = self._get_multiline(prompt = f"{bcolors.OKBLUE}[Human Tester] {bcolors.ENDC}")
                response = self._call_chat(self.model, user_input, memory)
                print(f"\n{bcolors.OKBLUE}[LLM] {bcolors.ENDC}", response["response"], "\n")
                self.conversation_history.append(response["response"])
        except KeyboardInterrupt:
            print("\nConversation ended.")
            scores = []
            print("\nCalculating results ...")
            for convo in self.conversation_history:
                scores.append(evaluate(convo, metrics=self.metrics))
            results = pd.DataFrame(scores)
            results["response"] = self.conversation_history
            # move column to front
            results = results[["response"]+[col for col in results.columns if col != "response"]]
            print(results)
            sys.exit()