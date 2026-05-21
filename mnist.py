from PIL import Image
import numpy as np
import torch as T
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt
device = T.device('cpu')  # Usar CPU directament
print(f"Executant en: {device}")

BATCH_SIZE = 23  # Imatges porcecades/hora
LEARNING_RATE = 0.001  # Velocitat de aprenetage
EPOCHS = 5  # Repeticions del Dataset

transform = transforms.Compose(
    [
        transforms.ToTensor(),  # Convertir a tensor
        transforms.Normalize((0.1307,), (0.3081,)),  # Normalitzar
    ]
)

train_Dataset = datasets.MNIST(
    root="./data", train=True, download=True, transform=transform
)

test_Dataset = datasets.MNIST(
    root="./data", train=False, download=True, transform=transform
)

trian_loader = DataLoader(train_Dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_Dataset, batch_size=BATCH_SIZE, shuffle=False)


print(f"✅ Dades carregades!")
print(f"   Imatges entrenament: {len(train_Dataset)}")
print(f"   Imatges test: {len(test_Dataset)}")


class Clasificador(nn.Module):
    def __init__(self):
        super(Clasificador, self).__init__()
        # Capes Lineals
        self.fc1 = nn.Linear(28 * 28, 128)  # Entrada: 784 neurodes (28x28 píxels)
        self.fc2 = nn.Linear(128, 64)  # Capa oculta: 128 → 64 neurodes
        self.fc3 = nn.Linear(64, 10)  # Sortida: 10 dígits (0-9)

        # Sortida: 10 dígits (0-9)
        self.relu = nn.ReLU()

        # Dropout (evita "sobreajustament")
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        # Capa 1
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        # Capa 2
        x = self.fc2(x)
        x = self.relu(x)
        x = self.dropout(x)
        # Capa 3
        x = self.fc3(x)

        return x


model = Clasificador().to(device)
print(f"\n✅ Model creat!")
print(model)


# Definir la funció de pérdua
criterion = nn.CrossEntropyLoss()
optimazer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

print(f"\n✅ Configuració d'entrenament llesta!")
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
        loss = criterion(outputs, labels)
        loss = criterion(outputs, labels)
        loss.backward()
        optimazer.step()
        total_loss += loss.item()
        _, predicted = T.max(outputs, 1)
        correct += (predicted == labels).sum().item()
        total = labels.size(0)

    accuracy = 100 * correct / total
    avg_loss = total_loss / len(train_loader)
    return avg_loss, accuracy


def validar(model, test_loader, criterion, device):
    model.eval()
    total_loss = 0
    correct = 0
    total = 0
    with T.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            total_loss += loss.item()
            _, predicted = T.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total = labels.size(0)

        accuracy = 100 * correct / total
        avg_loss = total_loss / len(test_loader)
        return avg_loss, accuracy  


print(f"\n✅ Funcions d'entrenament creades!")

train_losses = []
train_accuracy = []
test_losses = []
test_accuracy = []

print(f"\n🚀 Començant entrenament...")
print(f"   Epochs: {EPOCHS}")
print(f"   Batches per epoch: {len(trian_loader)}")
print("-" * 60)

for epoch in range(EPOCHS):
    train_loss, train_acc = entrenar_epoch(model, trian_loader, criterion, optimazer, device)
    test_loss, test_acc = validar(model, test_loader, criterion, device)
    train_losses.append(train_loss)
    train_accuracy.append(train_acc)
    test_losses.append(test_loss)
    test_accuracy.append(test_acc)
    print(f"Epoch [{epoch+1}/{EPOCHS}]")
    print(f"  Train → Loss: {train_loss:.4f}, Acurácia: {train_acc:.2f}%")
    print(f"  Test  → Loss: {test_loss:.4f}, Acurácia: {test_acc:.2f}%")
    print("-" * 60)

print(f"\n✅ Entrenament completat!")

fig, axes = plt.subplots(1,2, figsize=(12,4))
axes[0].plot(train_losses, label = "Train_losses", marker = "o")
axes[0].plot(test_losses, label = "Test_losses", marker = "s")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Loss")
axes[0].set_title("Perdua durant l'entenament")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(train_accuracy, label = "Train Accuracy", marker = "o")
axes[1].plot(test_losses, label = "Test Accuracy", marker = "s")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Train Accuracy")
axes[1].set_title("Perdua durant l'entenament")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()

print(f"\n📊 Estadístiques finals:")
print(f"   Train Loss final: {train_losses[-1]:.4f}")
print(f"   Test Loss final: {test_losses[-1]:.4f}")
print(f"   Train Accuracy final: {train_accuracy[-1]:.2f}%")
print(f"   Test Accuracy final: {test_accuracy[-1]:.2f}%")

def predir_digit(model, image_path, device):
    img = Image.open(image_path).convert("L")
    img = img.resize((28, 28))
    img_tensor = transforms.ToTensor()(img)
    img_tensor = transforms.Normalize((0.1307,), (0.3081,))(img_tensor)
    img_tensor = img_tensor.unsqueeze(0).to(device)
    model.eval()
    with T.no_grad():
        pass
