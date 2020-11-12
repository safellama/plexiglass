import torch

def test_robustness(model, attack, dataloader, device):
    for images, labels in dataloader:
        perturbed_images = attack(images, labels).to(device)
        outputs = model(perturbed_images)
        labels = labels.to(device)

        _, pre = torch.max(outputs.data, 1)
        total += 1
        correct += (pre == labels).sum()
    return (100 * float(correct) / total)
