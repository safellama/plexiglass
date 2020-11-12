# torch-safetynet
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

SafetyNet is a PyTorch toolbox for cybersecurity research and testing against adversarial attacks and deepfakes. 

## Usage

```python
import torch
import torch.nn as nn
from safetynet.adversarial import FGSM

# ... ... ... #
# load model  #
# ... ... ... #

# fast_gradient_sign_method
model.eval()
attack = FGSM(model=model, loss = nn.CrossEntropyLoss(), eps=0.001)

for images, labels in loader:
    perturbed_images = attack(images, labels).to(device)
    outputs = model(perturbed_images)
    labels = labels.to(device)

    # calculate accuracy
```