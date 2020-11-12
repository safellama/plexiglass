import torch
from plexiglass.adversarial.fgsm import FGSM

def test_robustness(model, attack, dataloader, device, eps=None):

    # normal run 
    for images, labels in dataloader:
            outputs = model(images.to(device))
            labels = labels.to(device)

            _, pre = torch.max(outputs.data, 1)
            total += 1
            correct += (pre == labels).sum()
    print('Accuracy: '+ str(100 * float(correct) / total))

    # attack run 

    if isinstance(model, FGSM()):
        for ep in eps:
            for images, labels in dataloader:   
                perturbed_images = attack(images, labels).to(device)
                outputs = model(perturbed_images)
                labels = labels.to(device)

                _, pre = torch.max(outputs.data, 1)
                total += 1
                correct += (pre == labels).sum()
            print('Epsilon: '+str(ep)+' Accuracy: '+str(100 * float(correct) / total))
    else:
        for images, labels in dataloader:
            perturbed_images = attack(images, labels).to(device)
            outputs = model(perturbed_images)
            labels = labels.to(device)

            _, pre = torch.max(outputs.data, 1)
            total += 1
            correct += (pre == labels).sum()
        print('Accuracy: '+ str(100 * float(correct) / total))
