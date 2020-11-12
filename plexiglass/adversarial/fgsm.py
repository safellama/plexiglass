import torch

class FGSM:
    def __init__(self, model, loss, device):
        self.device = device
        self.model = model
        self.loss = loss

    def __call__(self, images, labels, eps):

        images = images.to(self.device)
        labels = labels.to(self.device)
        images.requires_grad = True 
                
        outputs = self.model(images)
        
        self.model.zero_grad()
        cost = self.loss(outputs, labels).to(self.device)
        cost.backward()
        
        return torch.clamp(images + eps*images.grad.sign(), 0, 1)
        