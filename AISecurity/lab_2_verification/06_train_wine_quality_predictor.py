import argparse
import os
import idx2numpy
import numpy as np
import pandas as pd
from torch.utils.data import DataLoader, TensorDataset

parser = argparse.ArgumentParser()
parser.add_argument("--epochs", type=int, default=5)
args = parser.parse_args()

BATCH_SIZE = 64

# data loading
df = pd.read_csv("data/wine/wine_data.csv").drop(columns=["Id"])
y = df["quality"].clip(1, 8).to_numpy(dtype=np.int64) - 1 # bring to 0-based index
X = df.drop(columns=["quality"]).to_numpy(dtype=np.float32) # all features, leave feature selection unsolved
X = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0) + 1e-8) # normalize features (all are numerical)

# create IDX files for Vehicle verification
N_VERIFY = 20
os.makedirs("data/wine", exist_ok=True)
idx2numpy.convert_to_file("data/wine/wine-features.idx", X[:N_VERIFY].astype(np.float64))
idx2numpy.convert_to_file("data/wine/wine-labels.idx", y[:N_VERIFY].astype(np.uint8))

# training
import torch
from tqdm import tqdm
import torch.nn as nn

train_loader = DataLoader(
    TensorDataset(torch.from_numpy(X), torch.from_numpy(y)),
    batch_size=BATCH_SIZE,
    shuffle=True,
)

model = nn.Sequential(
    nn.Linear(11, 16),
    nn.ReLU(),
    nn.Linear(16, 8),
    nn.ReLU(),
    nn.Linear(8, 8),
)

optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
cross_entropy = nn.CrossEntropyLoss()

num_epochs = args.epochs

for epoch in tqdm(range(num_epochs)):
    running_loss, correct, seen = 0.0, 0, 0

    for features, labels in train_loader:
        optimizer.zero_grad()
        logits = model(features)
        loss = cross_entropy(logits, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * labels.numel()
        correct += (logits.argmax(1) == labels).sum().item()
        seen += labels.numel()

    print(f"Epoch: {epoch + 1}, mean loss: {running_loss / seen:.4f}, "
          f"train accuracy: {100 * correct / seen:.1f}%")

# Saving in ONNX format
model.eval()

try:
    os.mkdir("onnx_models")
except FileExistsError:
    pass
finally:
    torch.onnx.export(
        model,
        torch.randn(1, 11),
        "onnx_models/wine_classifier.onnx",
        input_names=["input"],
        output_names=["output"],
        opset_version=12,
        dynamo=False,
        external_data=False,
    )
    torch.onnx.export(
        model,
        torch.randn(1, 11),
        f"onnx_models/wine_classifier_{args.epochs}_epochs.onnx",
        input_names=["input"],
        output_names=["output"],
        opset_version=12,
        dynamo=False,
        external_data=False,
    )
