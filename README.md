<h1 align="center">
<img src="plexiglass/assets/plexiglass.png" width="80" height="80"><br>
Plexiglass</h1>
<p align="center">
Wondering if your AI model is safe enough to use? Plexiglass is your sparring partner to bolster your model's defenses!<br><br>
<a href="https://badge.fury.io/py/plexiglass"><img src="https://badge.fury.io/py/plexiglass.svg" alt="PyPI version" height="18"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-apache2.0-yellow.svg" alt="license MIT" height="18"></a>
</p>
<!-- <p align="center">A Python Machine Learning Security Toolbox for Adversarial Attacks. Works with LLMs, DNNs, and other machine learning algorithms.</p> -->

## What is Plexiglass?

Plexiglass is a Python toolbox which supports pentesting against adversarial attacks in machine learning. It has two modules: LLMs and DNNs. For LLMs, plexiglass uses [litellm](https://github.com/BerriAI/litellm) under the hood. 

We are working tirelessly to include more frameworks and attack/ defense mechanisms for testing. Please read our docs for the latest updates.

> [!IMPORTANT]
> We are looking for contributors! Fork the repo to get started. Contribution guide is coming soon.

> [!NOTE]
> Plexiglass is open-source: Please leave a star to support the project! ⭐

## What is Adversarial Machine Learning?

Adversarial machine learning involves manipulating input data to deceive machine learning models. In deep neural networks (DNNs) and large language models (LLMs), attacks include adding subtly modified inputs that cause incorrect model predictions or responses. These attacks exploit model vulnerabilities, testing their robustness and security.

## Installation

The first experimental release is version `0.0.1`.

To download the package from PyPi:

`pip install --upgrade plexiglass`

## Getting Started

### LLM Module: Simple Usage

We support a variety of LLMs using `litellm`. Alternatively, you can also test your own `huggingface` models.

```python
from plexiglass.LLM.evaluate import evaluate
from plexiglass.model import Model

import os

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
model = Model("openai", "gpt-3.5-turbo")

evaluate(model, metrics=["toxicity"], attacks=["prompt_injection", "gcg"])
```

### DNN Module: Simple Usage

Here is an example on how to test a model's robustness on FGSM attacks:

```python
from plexiglass.DNN.evaluate import evaluate
from plexiglass.model import Model

import os

# load your pytorch model here

model = Model("torch", your-model)

evaluate(model, metrics=["accuracy"], attacks=["fgsm"])
```

### Feature Request
To request new features, please submit an [issue](https://github.com/enochkan/plexiglass/issues)

### Local Development

To get started

```python
make develop
```

this will clean, build, and install the package locally for development purpose.

### Contributors

<!-- Copy-paste in your Readme.md file -->

<a href="https://github.com/kortex-labs/plexiglass/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kortex-labs/plexiglass" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
