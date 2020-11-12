# plexiglass
[![PyPI version](https://badge.fury.io/py/plexiglass.svg)](https://badge.fury.io/py/plexiglass)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Plexiglass is a PyTorch toolbox for cybersecurity research and testing against adversarial attacks and deepfakes. 

## :arrow_down: Installation

Right now, `plexiglass` works with `python <=3.8.3`. 

To download the package from PyPi:

```pip install --upgrade plexiglass```

## :bookmark_tabs: Usage

Tl:dr `plexiglass.adversarial` contains adversarial attacks and `plexiglass.detectors` contains deepfake detectors. Please refer to (demo.ipynb)[https://github.com/enochkan/plexiglass/blob/main/demo.ipynb] for a detailed example.

### Simple Usage

A simple way to test a model's robustness to adversarial attacks is to call `test_robustness`, which outputs a model's accuracy before and after the attack. 

```python
import torch
import torch.nn as nn
from plexiglass.adversarial import FGSM, test_robustness 

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

### Manual Testing

Alternatively, you can call the predefined method of attack to get the perturbed image for manual testing functions.

```python
import torch
import torch.nn as nn
from plexiglass.adversarial import FGSM, test_robustness

device = torch.device("cuda" if use_cuda else "cpu")

# ... ... ... #
# load model  #
# ... ... ... #

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

### Deepfake Detection

Deepfake detectors are also available for training in Plexiglass. 

```python
import torch
import torch.nn as nn
from plexiglass.detectors import MesoInception

model = MesoInception()
```