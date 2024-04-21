import torch
import torch.nn as nn
import torch.nn.functional as F

class mlpModel_64(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3*64*64, 100)
        self.fc2 = nn.Linear(100, 50)
        self.out = nn.Linear(50, 2)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.out(x)
        return x

class cnnModel1_64(nn.Module):
    def __init__(self):
        super().__init__()
        # Layer 1: 3*64*64 -> 8*31*31
        self.conv_1 = nn.Conv2d(
            in_channels=3, 
            out_channels=8, 
            kernel_size=3,
            stride=1
        )
        self.batchnorm_1 = nn.BatchNorm2d(
            num_features=8
        )
        self.maxpool_1 = nn.MaxPool2d(
            kernel_size=2, 
            stride=2,
            padding=0
        )
        # Layer 2: 8*31*31 -> 16*14*14
        self.conv_2 = nn.Conv2d(
            in_channels=8, 
            out_channels=16, 
            kernel_size=3,
            stride=1
        )
        self.batchnorm_2 = nn.BatchNorm2d(
            num_features=16
        )
        self.maxpool_2 = nn.MaxPool2d(
            kernel_size=2,
            stride=2,
            padding=0
        )
        # Layer 3: 16*14*14 -> 32*13*13
        self.conv_3 = nn.Conv2d(
            in_channels=16,
            out_channels=32,
            kernel_size=3,
            stride=1
        )
        self.batchnorm_3 = nn.BatchNorm2d(
            num_features=32
        )
        self.maxpool_3 = nn.MaxPool2d(
            kernel_size=2,
            stride=2,
            padding=0
        )
        # Layer 4: 32*13*13 -> 64*7*7
        self.conv_4 = nn.Conv2d(
            in_channels=32,
            out_channels=64,
            kernel_size=3,
            stride=1,
            padding=1
        )
        self.batchnorm_4 = nn.BatchNorm2d(
            num_features=64
        )
        self.maxpool_4 = nn.MaxPool2d(
            kernel_size=2,
            stride=2,
            padding=1
        )
        # Layer 5: 64*7*7 -> 128*5*5
        self.conv_5 = nn.Conv2d(
            in_channels=64,
            out_channels=128,
            kernel_size=3,
            stride=1,
            padding=1
        )
        self.batchnorm_5 = nn.BatchNorm2d(
            num_features=128
        )
        self.maxpool_5 = nn.MaxPool2d(
            kernel_size=2,
            stride=2,
            padding=1
        )
        # Layer 6: 128*5*5 -> 256*4*4
        self.conv_6 = nn.Conv2d(
            in_channels=128,
            out_channels=256,
            kernel_size=3,
            stride=1,
            padding=1
        )
        self.batchnorm_6 = nn.BatchNorm2d(
            num_features=256
        )
        self.maxpool_6 = nn.MaxPool2d(
            kernel_size=2,
            stride=2,
            padding=1
        )
        # Layer 7: 256*4*4 -> 512*3*3
        self.conv_7 = nn.Conv2d(
            in_channels=256,
            out_channels=512,
            kernel_size=3,
            stride=1,
            padding=1
        )
        self.batchnorm_7 = nn.BatchNorm2d(
            num_features=512
        )
        self.maxpool_7 = nn.MaxPool2d(
            kernel_size=2,
            stride=2,
            padding=1
        )
        self.dropout_1 = nn.Dropout2d(
            p=0.5
        )
        # Layer 8: 512*3*3 -> 100*1*1
        self.fc_1 = nn.Linear(
            in_features=2*2*512,
            out_features=100
        )
        self.dropout_2 = nn.Dropout1d(
            p=0.5
        )
        # Layer 9: 100*1*1 -> 50*1*1
        self.fc_2 = nn.Linear(
            in_features=100,
            out_features=50
        )
        self.dropout_3 = nn.Dropout1d(
            p=0.5
        )
        # Output Layer: 50*1*1 -> 2*1*1
        self.fc_3 = nn.Linear(
            in_features=50, 
            out_features=2
        )

    def forward(self, x):
        # Layer 1
        x = self.conv_1(x)
        x = self.batchnorm_1(x)
        x = F.relu(x)
        x = self.maxpool_1(x)

        # Layer 2
        x = self.conv_2(x)
        x = self.batchnorm_2(x)
        x = F.relu(x)
        x = self.maxpool_2(x)

        # Layer 3
        x = self.conv_3(x)
        x = self.batchnorm_3(x)
        x = F.relu(x)
        x = self.maxpool_3(x)

        # Layer 4
        x = self.conv_4(x)
        x = self.batchnorm_4(x)
        x = F.relu(x)
        x = self.maxpool_4(x)

        # Layer 5
        x = self.conv_5(x)
        x = self.batchnorm_5(x)
        x = F.relu(x)
        x = self.maxpool_5(x)

        # Layer 6
        x = self.conv_6(x)
        x = self.batchnorm_6(x)
        x = F.relu(x)
        x = self.maxpool_6(x)

        # Layer 7
        x = self.conv_7(x)
        x = self.batchnorm_7(x)
        x = F.relu(x)
        x = self.maxpool_7(x)
        x = self.dropout_1(x)

        # Layer 8
        x = torch.flatten(x, 1)
        x = self.fc_1(x)
        x = F.relu(x)
        x = self.dropout_2(x)

        # Layer 9
        x = self.fc_2(x)
        x = F.relu(x)
        x = self.dropout_3(x)

        # Output Layer
        x = self.fc_3(x)
        x = F.softmax(x, dim=1)

        return x
    
class cnnModel2_64(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 13 * 13, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
class cnnModel3_128(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_1 = nn.Conv2d(
            in_channels=1,
            out_channels=16,
            kernel_size=3,
            stride=1
        )
        self.maxpool_1 = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )
        self.conv_2 = nn.Conv2d(
            in_channels=16,
            out_channels=32,
            kernel_size=3,
            stride=1
        )
        self.maxpool_2 = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )
        self.conv_3 = nn.Conv2d(
            in_channels=32,
            out_channels=64,
            kernel_size=3,
            stride=1
        )
        self.maxpool_3 = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )
        self.conv_4 = nn.Conv2d(
            in_channels=64,
            out_channels=128,
            kernel_size=3,
            stride=1
        )
        self.maxpool_4 = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )
        self.fc_1 = nn.Linear(
            in_features=6*6*128,
            out_features=4096
        )
        self.fc_2 = nn.Linear(
            in_features=4096,
            out_features=4096
        )
        self.fc_3 = nn.Linear(
            in_features=4096,
            out_features=2
        )

    def forward(self, x):
        x = self.conv_1(x)
        x = F.relu(x)
        x = self.maxpool_1(x)
        
        x = self.conv_2(x)
        x = F.relu(x)
        x = self.maxpool_2(x)

        x = self.conv_3(x)
        x = F.relu(x)
        x = self.maxpool_3(x)

        x = self.conv_4(x)
        x = F.relu(x)
        x = self.maxpool_4(x)

        x = torch.flatten(x, 1)
        x = self.fc_1(x)
        x = F.relu(x)

        x = self.fc_2(x)
        x = F.relu(x)

        x = self.fc_3(x)
        x = F.softmax(x, dim=1)

        return x