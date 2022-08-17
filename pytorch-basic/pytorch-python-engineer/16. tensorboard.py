import os
import sys
import warnings
warnings.filterwarnings(action='ignore')

if os.getcwd() == '/content':
    data_path = '/content/drive/MyDrive/Colab Notebooks/datasets'
else:
    data_path = r'G:\내 드라이브\Colab Notebooks\datasets'


import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# tensorboard writer
writer = SummaryWriter('runs/mnist')

# device config
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# hyper-params
input_size = 784 # 28 x 28
hidden_size = 100
num_classes = 10
num_epochs = 2
batch_size = 100
learning_rate = 0.001

# MNIST
train_dataset = datasets.MNIST(root=data_path, train=True, download=True,
                               transform=transforms.ToTensor())
test_dataset = datasets.MNIST(root=data_path, train=False, download=True,
                              transform=transforms.ToTensor())

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size,
                          shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size,
                         shuffle=False)

example_data, example_targets = next(iter(test_loader))

# tensorboard
img_grid = torchvision.utils.make_grid(example_data)
writer.add_image('mnist_images', img_grid)
writer.close()
# sys.exit()

# build model
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        return out

model = NeuralNet(input_size, hidden_size, num_classes)

# loss & optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# model graph
writer.add_graph(model, example_data.reshape(-1, 28*28))
writer.close()
sys.exit()

# training loop
n_total_steps = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        
        # (100, 1, 28, 28) -> (100, 784)
        images = images.reshape(-1, 28*28).to(device)
        laebls = labels.to(device)
        
        # forward
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # backwards
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i+1) % 100 == 0:
            print(f'epoch {epoch+1} / {num_epochs}, step {i+1}/{n_total_steps}, loss = {loss.item():.4f}')

# test
with torch.no_grad():
    n_correct = 0
    n_samples = 0
    for images, labels in test_loader:
        images = images.reshape(-1, 28*28).to(device)
        laebls = labels.to(device)
        
        outputs = model(images)
        
        # value, index
        _, preidcitions = torch.max(outputs, 1)
        n_samples += labels.shape[0]
        n_correct = (preidcitions == labels).sum().item()
    
    acc = 100.0 * n_correct / n_samples
    print(f'accuracy : {acc}')