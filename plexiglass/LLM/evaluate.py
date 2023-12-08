from detoxify import Detoxify

def measure_toxicity(prompt: str):
    return Detoxify('original').predict(prompt)

def evaluate(model, metrics: list = ["toxicity"], attacks: list = ["prompt_injection"]):
    results = []
    for metric in metrics:
        if metric == "toxicity":
            results.append(measure_toxicity(prompt))
        else:
            pass