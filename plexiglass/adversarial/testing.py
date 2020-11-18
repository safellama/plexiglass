import torch
from .fgsm import FGSM

def test_robustness(attack, dataloader, device, eps=None):
    total, correct = 0, 0
    # normal run 
    for images, labels in dataloader:
            outputs = attack.model(images.to(device))
            labels = labels.to(device)

            _, pre = torch.max(outputs.data, 1)
            total += 1
            correct += (pre == labels).sum()
    print('Accuracy: '+ str(100 * float(correct) / total))

    # attack run 

    if type(attack) == type(FGSM(model=None, loss=None, device=None)):
        for ep in eps:
            total, correct = 0, 0
            for images, labels in dataloader:   
                perturbed_images = attack(images, labels, ep).to(device)
                outputs = attack.model(perturbed_images)
                labels = labels.to(device)

                _, pre = torch.max(outputs.data, 1)
                total += 1
                correct += (pre == labels).sum()
            print('Epsilon: '+str(ep)+' Accuracy: '+str(100 * float(correct) / total))
    else:
        total, correct = 0, 0
        for images, labels in dataloader:
            perturbed_images = attack(images, labels).to(device)
            outputs = attack.model(perturbed_images)
            labels = labels.to(device)

            _, pre = torch.max(outputs.data, 1)
            total += 1
            correct += (pre == labels).sum()
        print('Accuracy: '+ str(100 * float(correct) / total))
