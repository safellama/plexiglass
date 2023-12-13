import json

# TODO: resolve prompts path to relative path
def basic_injection(model, prompts_path = "./plexiglass/LLM/attacks/injection/adversarial_prompts.jsonl"):
    # try:
    with open(prompts_path, 'r') as jsonl_file:
        results, prompts_used = [], []
        for line in list(jsonl_file):
            # Parse each line as a JSON object
            prompt = json.loads(line.strip())["prompt"]
            prompts_used.append(prompt)
            results.append(model.prompt([prompt]))
        return results, prompts_used
    
    # except FileNotFoundError:
    #     print(f"File not found: {prompts_path}")
    # except Exception as e:
    #     print(f"Error processing file: {e}")