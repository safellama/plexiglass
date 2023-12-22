from detoxify import Detoxify
from plexiglass.core.red.injection import basic_injection 
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import pandas as pd

def evaluate_toxcity(prompt: str):
    return Detoxify('original').predict(prompt)

def evaluate_pii(prompt: str):
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    ner_results = nlp(prompt)
    return ner_results


def evaluate(prompt, metrics: list = ["toxicity", "pii"]):
    results = {}
    for metric in metrics:
        if metric == "toxicity":
            toxicity = evaluate_toxcity(prompt)
            results.update(toxicity)
        elif metric == "pii":
            pii = evaluate_pii(prompt)
            results.update({"pii_detected": pii})
    return results

if __name__ == "__main__":
    evaluate()