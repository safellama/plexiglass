from plexiglass.LLM.model import KorrectModel
import pandas as pd
import requests
import time

class PlexiglassModel:
    def __init__(self, parameters: dict):
        self.parameters = parameters
        self.models = []
        self.results = pd.DataFrame()
        
    def measure_latency(self, func, *args, **kwargs):
        try:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            latency_ms = (end_time - start_time) * 1000
            return latency_ms, result

        except Exception as e:
            print(f"Error: {e}")
            return None, None

    def run(self):
        for model in self.parameters["models"]:
            self.models.append(KorrectModel(model_name=model["model_name"], model_type=model["model_type"]))
        
        for model in self.models:
            latency_ms, result = self.measure_latency(model.prompt, [{"role": "user", "content": self.parameters["prompt"]}])
            self.results = pd.concat([self.results, pd.DataFrame({"model_name":[model.model_name], "model_type":[model.model_type], "latency":[latency_ms], "result":[result]})])
        return self.results
