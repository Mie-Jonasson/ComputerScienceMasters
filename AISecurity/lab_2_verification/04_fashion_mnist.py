import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Subset
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--robust", action="store_true")
parser.add_argument("--specification", type=str, default="fmnist-robustness.vcl")
args = parser.parse_args()

BATCH_SIZE = 64
SUBSET_SIZE = 1024  # ensure SUBSET_SIZE mod BATCH_SIZE == 0

# data loading
transform = transforms.Compose([
    transforms.ToTensor()
])

train_data = torchvision.datasets.FashionMNIST(
    root="./data", train=True, download=True, transform=transform
)
train_loader = DataLoader(
    Subset(train_data, range(SUBSET_SIZE)), batch_size=BATCH_SIZE, shuffle=True
)

# training
import torch
from tqdm import tqdm
import torch.nn as nn

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784, 64),
    nn.ReLU(),
    nn.Linear(64, 32),
    nn.ReLU(),
    nn.Linear(32, 10)
)

optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
cross_entropy = nn.CrossEntropyLoss()

num_epochs = 5  # the script ships with 5; the table below uses 75, 100 and 150

if args.robust:
    import vehicle_lang as vcl
    from vehicle_lang.loss import pytorch as loss_pt

    spec = loss_pt.load_specification(
        args.specification,
        logic=vcl.VehicleDifferentiableLogic(),
    )

    constraint_loss_fn = spec["robust"]

    def network(x: torch.Tensor) -> torch.Tensor:
        return model(x.reshape(1, 1, 28, 28)).reshape(10)

    alpha = 0.5

    for epoch in tqdm(range(num_epochs)):
        for step, (images, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            logits = model(images)
            loss = cross_entropy(logits, labels)

            constraint_loss = constraint_loss_fn(
                n=BATCH_SIZE,
                classifier=network,
                epsilon=torch.tensor(0.005),
                trainingImages=images.squeeze(1),
                trainingLabels=labels
            )

            constraint_loss = torch.stack(constraint_loss).mean()
            total_loss = alpha * loss + (1 - alpha) * constraint_loss

            total_loss.backward()
            optimizer.step()

else:

    for epoch in tqdm(range(num_epochs)):
        running_loss, correct, seen = 0.0, 0, 0

        for images, labels in train_loader:
            optimizer.zero_grad()
            logits = model(images)
            loss = cross_entropy(logits, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * labels.numel()
            correct += (logits.argmax(1) == labels).sum().item()
            seen += labels.numel()

        print(f"Epoch: {epoch + 1}, mean loss: {running_loss / seen:.4f}, "
            f"train accuracy: {100 * correct / seen:.1f}%")

# Saving in ONNX format
import os

model.eval()

try:
    os.mkdir('onnx_models')
finally:
    if args.robust:
        torch.onnx.export(
            model,
            torch.randn(1,1,28,28),
            "classifier.onnx", # file name
            external_data=False, # required for Marabou verification
        )
    else:
        torch.onnx.export(
            model,
            torch.randn(1, 1, 28, 28),
            "onnx_models/vanilla_classifier.onnx",
            input_names=["input"],
            output_names=["output"],
            opset_version=12,  # Marabou 1.0 cannot parse the default opset 20
            dynamo=False,
            external_data=False,  # required for Marabou verification
        )
