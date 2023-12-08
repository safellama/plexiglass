from detoxify import Detoxify

def measure_toxicity(prompt: str):
    return Detoxify.predict(prompt)

def eval(prompt, metrics: list = ["toxicity"]):
    results = []
    for metric in metrics:
        if metric == "toxicity":
            results.append(measure_toxicity(prompt))
        else:
            pass