import torch

class PGD:
    def __init__(self, model, device):
        self.device = device
        self.model = model
        self.loss = nn.CrossEntropyLoss()

    def __call__(self, images, labels, eps=0.3, alpha=2/255, iterations=100):
        
        images = images.to(device)
        labels = labels.to(device)
            
        ori_images = images.data
            
        for i in range(iterations) :    
            images.requires_grad = True
            outputs = self.model(images)

            model.zero_grad()
            cost = self.loss(outputs, labels).to(device)
            cost.backward()

            adv_images = images + alpha*images.grad.sign()
            eta = torch.clamp(adv_images - ori_images, min=-eps, max=eps)            
        return torch.clamp(ori_images + eta, min=0, max=1).detach_()