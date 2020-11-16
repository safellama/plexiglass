import torch

class PGD:
    def __init__(self, model, loss, device):
        self.device = device
        self.model = model
        self.loss = loss

    def __call__(self, images, labels, eps=0.3, alpha=2/255, iters=40):

        images = images.to(device)
        labels = labels.to(device)
        loss = nn.CrossEntropyLoss()
            
        ori_images = images.data
            
        for i in range(iters) :    
            images.requires_grad = True
            outputs = self.model(images)

            model.zero_grad()
            cost = loss(outputs, labels).to(device)
            cost.backward()

            adv_images = images + alpha*images.grad.sign()
            eta = torch.clamp(adv_images - ori_images, min=-eps, max=eps)            
        return torch.clamp(ori_images + eta, min=0, max=1).detach_()