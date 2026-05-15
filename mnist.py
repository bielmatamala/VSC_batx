import torch as T
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# import matplotlib.pyplot as plt

device = T.device("cuda" if T.cuda.is_available else "cpu")
print(f"Executant en: {device}")

BATCH_SIZE = 23  # Imatges porcecades/hora
LEARNING_RATE = 0.001  # Velocitat de aprenetage
EPOCHS = 5  # Repeticions del Dataset

transform = transforms.Compose(
    [
        transforms.ToTensor(),  # Convertir a tensor
        transforms.Normalize((0.1307,), (0.3081,)),# Normalitzar
    ]
)

train_Dataset = datasets.MNIST(
    root="./data", train=True, download=True, transform=transform
)

test_Dataset = datasets.MNIST(
    root = "./data",
    train = False,
    download = True,
    transform = transform
)

trian_loader = DataLoader(train_Dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_Dataset, batch_size=BATCH_SIZE, shuffle=False)


print(f"✅ Dades carregades!")
print(f"   Imatges entrenament: {len(train_Dataset)}")
print(f"   Imatges test: {len(test_Dataset)}")

class Clasificador(nn.modules):
    def __init__(self):
        super(Clasificador,self).__init__()
        #Capes Lineals
        self.fc1 = nn.Linear(28*28, 128) # Entrada: 784 neurodes (28x28 píxels)
        self.fc2 = nn.Linear(128, 64) # Capa oculta: 128 → 64 neurodes
        self.fc3 = nn.Linear(64,10) # Sortida: 10 dígits (0-9)

        # Sortida: 10 dígits (0-9)
        self.relu = nn.ReLU()

        # Dropout (evita "sobreajustament")
        self.dropout = nn.Dropout(0.2)
    
    def Forward(self, x):
        x = x.view(-1,28*28)
        #Capa 1
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        #Capa 2
        x = self.fc2(x)
        x = self.relu(x)
        x = self.dropout(x)
        #Capa 3
        x = self.fc3(x)

        return x
    
model = Clasificador().to(device)
print(f"\n✅ Model creat!")
print(model)


# Definir la funció de pérdua
criterion = nn.CrossEntropyLoss()
optimazer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

print(f"\n✅ Configuració d'entrenament lista!")
print(f"   Loss: CrossEntropyLoss")
print(f"   Optimitzador: Adam")
print(f"   Learning rate: {LEARNING_RATE}")

def entrenar_epoch(model, train_loader, criterion, optimizer, device):
    model.train()
    total_loss = 0
    correct = 0 
    total = 0

    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)
        optimazer.zero_grad()
        outputs = model(images)