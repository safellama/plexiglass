import torch

class FGSM:
    def __init__(self, model, loss, eps):
        self.device = torch.device("cuda" if use_cuda else "cpu")
        self.model = model
        self.loss = loss
        self.eps = eps

    def __call__(self, images, labels):
        images = images.to(self.device)
        labels = labels.to(self.device)
        images.requires_grad = True
                
        outputs = self.model(images)
        
        self.model.zero_grad()
        cost = self.loss(outputs, labels).to(self.device)
        cost.backward()
        
        return torch.clamp(images + self.eps*images.grad.sign(), 0, 1)
        
