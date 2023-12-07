<h1 align="center">
<img src="assets/plexiglass.png" width="80" height="80"><br>
Plexiglass</h1>
<p align="center">
<a href="https://badge.fury.io/py/plexiglass"><img src="https://badge.fury.io/py/plexiglass.svg" alt="PyPI version" height="18"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-apache2.0-yellow.svg" alt="license MIT" height="18"></a>
</p>
<p align="center">a toolbox for testing against adversarial attacks in DNNs and LLMs. </p>

## What is Plexiglass?

Plexiglass is a Python research toolbox which supports adversarial testing in deep learning. It has two modules: DNN and LLM. We currently support the following frameworks:

### DNNs
- torch

### LLMs
- OpenAI 

We are working tirelessly to include more frameworks and attack/ defense mechanisms for testing. Please read our docs for the latest updates.

> [!NOTE]
> Plexiglass is open-source: Please leave a star to support the project! ⭐

## What is Adversarial Machine Learning?

Adversarial machine learning involves manipulating input data to deceive machine learning models. In deep neural networks (DNNs) and large language models (LLMs), attacks include adding subtly modified inputs that cause incorrect model predictions or responses. These attacks exploit model vulnerabilities, testing their robustness and security.

## Installation

The first stable release is version `1.2.0`.

To download the package from PyPi:

`pip install --upgrade plexiglass`

## Getting Started

### DNN Module: Simple Usage

A simple way to test a deep neural network's robustness to adversarial attacks is to call `test_robustness`, which outputs a DNN's accuracy before and after the attack.

```python
import torch
import torch.nn as nn
from plexiglass.DNN.attacks import FGSM, test_robustness

device = torch.device("cuda" if use_cuda else "cpu")

# ... ... ... #
# load model  #
# ... ... ... #

# fast_gradient_sign_method
model.eval()
attack = FGSM(model=model, loss = nn.CrossEntropyLoss(), eps=0.001, device=device)

# single test_robustness to calculate model accuracy given attack method
accuracy = test_robustness(model=model, attack=attack, dataloader=loader, device=device)
```

### DNN Module: Manual Testing

Alternatively, you can call the predefined method of attack to get the perturbed image for manual testing functions.

```python
import torch
import torch.nn as nn
from plexiglass.attacks import FGSM, test_robustness

device = torch.device("cuda" if use_cuda else "cpu")

# fast_gradient_sign_method
model.eval()
attack = FGSM(model=model, loss = nn.CrossEntropyLoss(), eps=0.001, device=device)

# alternatively, you can call attack to get the perturbed image
for images, labels in loader:
    perturbed_images = attack(images, labels).to(device)
    outputs = model(perturbed_images)
    labels = labels.to(device)

    # calculate accuracy
```

### DNN module: Deepfake Detection

Deepfake detectors are also available for training in Plexiglass. Currently, only MesoNet/ MesoInception are available for use.

```python
import torch
import torch.nn as nn
from plexiglass.defense import MesoInception

model = MesoInception()
```

### LLM Module: Simple Usage
> [!NOTE] 
> coming soon

### Feature Request
To request new features, please submit an [issue](https://github.com/enochkan/plexiglass/issues)

### Local Development

To get started

```python
make develop
```

this will clean, build, and install the package locally for development purpose.
