import torch
import torch.nn as nn

class MesoNet(nn.Module):
	def __init__(self, num_classes=2):
		super(MesoNet, self).__init__()
		self.num_classes = num_classes
		self.conv1 = nn.Conv2d(3, 8, 3, padding=1, bias=False)
		self.bn1 = nn.BatchNorm2d(8)
		self.relu = nn.ReLU(inplace=True)
		self.leakyrelu = nn.LeakyReLU(0.1)
		self.conv2 = nn.Conv2d(8, 8, 5, padding=2, bias=False)
		self.bn2 = nn.BatchNorm2d(16)
		self.conv3 = nn.Conv2d(8, 16, 5, padding=2, bias=False)
		self.conv4 = nn.Conv2d(16, 16, 5, padding=2, bias=False)
		self.maxpooling1 = nn.MaxPool2d(kernel_size=(2, 2))
		self.maxpooling2 = nn.MaxPool2d(kernel_size=(4, 4))
		self.dropout = nn.Dropout2d(0.5)
		self.fc1 = nn.Linear(16*8*8, 16)
		self.fc2 = nn.Linear(16, num_classes)

	def forward(self, input):
		x = self.conv1(input)
		x = self.relu(x)
		x = self.bn1(x)
		x = self.maxpooling1(x) 
		x = self.conv2(x) 
		x = self.relu(x)
		x = self.bn1(x)
		x = self.maxpooling1(x) 
		x = self.conv3(x) 
		x = self.relu(x)
		x = self.bn2(x)
		x = self.maxpooling1(x) 
		x = self.conv4(x) 
		x = self.relu(x)
		x = self.bn2(x)
		x = self.maxpooling2(x) 
		x = x.view(x.size(0), -1) 
		x = self.dropout(x)
		x = self.fc1(x) 
		x = self.leakyrelu(x)
		x = self.dropout(x)
		x = self.fc2(x)

		return x


class MesoInception(nn.Module):
	def __init__(self, num_classes=2):
		super(MesoInception, self).__init__()
		self.num_classes = num_classes

		self.Incption1_conv1 = nn.Conv2d(3, 1, 1, padding=0, bias=False)
		self.Incption1_conv2_1 = nn.Conv2d(3, 4, 1, padding=0, bias=False)
		self.Incption1_conv2_2 = nn.Conv2d(4, 4, 3, padding=1, bias=False)
		self.Incption1_conv3_1 = nn.Conv2d(3, 4, 1, padding=0, bias=False)
		self.Incption1_conv3_2 = nn.Conv2d(4, 4, 3, padding=2, dilation=2, bias=False)
		self.Incption1_conv4_1 = nn.Conv2d(3, 2, 1, padding=0, bias=False)
		self.Incption1_conv4_2 = nn.Conv2d(2, 2, 3, padding=3, dilation=3, bias=False)
		self.Incption1_bn = nn.BatchNorm2d(11)

		self.Incption2_conv1 = nn.Conv2d(11, 2, 1, padding=0, bias=False)
		self.Incption2_conv2_1 = nn.Conv2d(11, 4, 1, padding=0, bias=False)
		self.Incption2_conv2_2 = nn.Conv2d(4, 4, 3, padding=1, bias=False)
		self.Incption2_conv3_1 = nn.Conv2d(11, 4, 1, padding=0, bias=False)
		self.Incption2_conv3_2 = nn.Conv2d(4, 4, 3, padding=2, dilation=2, bias=False)
		self.Incption2_conv4_1 = nn.Conv2d(11, 2, 1, padding=0, bias=False)
		self.Incption2_conv4_2 = nn.Conv2d(2, 2, 3, padding=3, dilation=3, bias=False)
		self.Incption2_bn = nn.BatchNorm2d(12)

		self.conv1 = nn.Conv2d(12, 16, 5, padding=2, bias=False)
		self.relu = nn.ReLU(inplace=True)
		self.leakyrelu = nn.LeakyReLU(0.1)
		self.bn1 = nn.BatchNorm2d(16)
		self.maxpooling1 = nn.MaxPool2d(kernel_size=(2, 2))

		self.conv2 = nn.Conv2d(16, 16, 5, padding=2, bias=False)
		self.maxpooling2 = nn.MaxPool2d(kernel_size=(4, 4))

		self.dropout = nn.Dropout2d(0.5)
		self.fc1 = nn.Linear(16*8*8, 16)
		self.fc2 = nn.Linear(16, num_classes)


	def InceptionLayer1(self, input):
		x1 = self.Incption1_conv1(input)
		x2 = self.Incption1_conv2_1(input)
		x2 = self.Incption1_conv2_2(x2)
		x3 = self.Incption1_conv3_1(input)
		x3 = self.Incption1_conv3_2(x3)
		x4 = self.Incption1_conv4_1(input)
		x4 = self.Incption1_conv4_2(x4)
		y = torch.cat((x1, x2, x3, x4), 1)
		y = self.Incption1_bn(y)
		y = self.maxpooling1(y)

		return y

	def InceptionLayer2(self, input):
		x1 = self.Incption2_conv1(input)
		x2 = self.Incption2_conv2_1(input)
		x2 = self.Incption2_conv2_2(x2)
		x3 = self.Incption2_conv3_1(input)
		x3 = self.Incption2_conv3_2(x3)
		x4 = self.Incption2_conv4_1(input)
		x4 = self.Incption2_conv4_2(x4)
		y = torch.cat((x1, x2, x3, x4), 1)
		y = self.Incption2_bn(y)
		y = self.maxpooling1(y)

		return y

	def forward(self, input):
		x = self.InceptionLayer1(input) 
		x = self.InceptionLayer2(x) 

		x = self.conv1(x) 
		x = self.relu(x)
		x = self.bn1(x)
		x = self.maxpooling1(x) 

		x = self.conv2(x) 
		x = self.relu(x)
		x = self.bn1(x)
		x = self.maxpooling2(x) 

		x = x.view(x.size(0), -1) 
		x = self.dropout(x)
		x = self.fc1(x)
		x = self.leakyrelu(x)
		x = self.dropout(x)
		x = self.fc2(x)

		return x