from .fgsm import FGSM
import torch
import matplotlib.pyplot as plt

def test_robustness(attack, dataloader, device, eps=None, plot=False):

    if plot and type(attack) != type(FGSM(model=None, loss=None, device=None)):
        print('Please set plot to False when attack is not FGSM')
        return 

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
        epsilon, accuracies = [], []
        for ep in eps:
            total, correct = 0, 0
            for images, labels in dataloader:   
                perturbed_images = attack(images, labels, ep).to(device)
                outputs = attack.model(perturbed_images)
                labels = labels.to(device)

                _, pre = torch.max(outputs.data, 1)
                total += 1
                correct += (pre == labels).sum()
            epsilon.append(ep)
            accuracies.append(float(correct) / total)
            print('Epsilon: '+str(ep)+' Accuracy: '+str(float(correct) / total))
        
        # plotting
        plt.figure(figsize=(5,5))
        plt.plot(epsilons, accuracies, "*-")
        plt.yticks(np.arange(0, 1.1, step=0.1))
        plt.xticks(np.arange(min(epsilon), max(epsilon), step=0.05))
        plt.title("Accuracy vs Epsilon")
        plt.xlabel("Epsilon")
        plt.ylabel("Accuracy")
        plt.show()

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
