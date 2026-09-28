import argparse
import os
import idx2numpy
import numpy as np
import pandas as pd
from torch.utils.data import DataLoader, TensorDataset

parser = argparse.ArgumentParser()
parser.add_argument("--epochs", type=int, default=5)
parser.add_argument("--robust", action="store_true")
parser.add_argument("--specification", type=str, default="06_wine.vcl")
args = parser.parse_args()

BATCH_SIZE = 64

# data loading
df = pd.read_csv("data/wine/wine_data.csv").drop(columns=["Id"])
y = df["quality"].clip(1, 8).to_numpy(dtype=np.int64) - 1 # bring to 0-based index
X = df.drop(columns=["quality"]).to_numpy(dtype=np.float32) # all features, leave feature selection unsolved
X = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0) + 1e-8) # normalize features (all are numerical)

# create IDX files for Vehicle verification
N_VERIFY = 50
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
    drop_last=args.robust, # drop last batch if not divisible by batch size
)

model = nn.Sequential(
    nn.Linear(11, 32),
    nn.ReLU(),
    nn.Linear(32, 16),
    nn.ReLU(),
    nn.Linear(16, 8),
)

optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
cross_entropy = nn.CrossEntropyLoss()

num_epochs = args.epochs

if args.robust:
    import vehicle_lang as vcl
    from vehicle_lang.loss import pytorch as loss_pt

    spec = loss_pt.load_specification(
        args.specification,
        logic=vcl.VehicleDifferentiableLogic(),
    )
    constraint_loss_fn = spec["robust"]

    def network(x: torch.Tensor) -> torch.Tensor:
        return model(x.reshape(1, 11)).reshape(8)

    alpha = 0.5

    for epoch in tqdm(range(num_epochs)):
        running_loss, correct, seen = 0.0, 0, 0

        for features, labels in train_loader:
            optimizer.zero_grad()
            logits = model(features)
            loss = cross_entropy(logits, labels)

            constraint_loss = constraint_loss_fn(
                n=features.shape[0],
                classifier=network,
                epsilon=torch.tensor(0.005),
                trainingInputs=features,
                trainingLabels=labels,
            )
            constraint_loss = torch.stack(constraint_loss).mean()
            total_loss = alpha * loss + (1 - alpha) * constraint_loss

            total_loss.backward()
            optimizer.step()

            running_loss += total_loss.item() * labels.numel()
            correct += (logits.argmax(1) == labels).sum().item()
            seen += labels.numel()

        print(f"Epoch: {epoch + 1}, mean loss: {running_loss / seen:.4f}, "
              f"train accuracy: {100 * correct / seen:.1f}%")

else:
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
    if args.robust:
        out_name = "onnx_models/wine_robust_classifier.onnx"
        out_epochs = f"onnx_models/wine_robust_classifier_{args.epochs}_epochs.onnx"
    else:
        out_name = "onnx_models/wine_classifier.onnx"
        out_epochs = f"onnx_models/wine_classifier_{args.epochs}_epochs.onnx"

    torch.onnx.export(
        model,
        torch.randn(1, 11),
        out_name,
        input_names=["input"],
        output_names=["output"],
        opset_version=12,
        dynamo=False,
        external_data=False,
    )
    torch.onnx.export(
        model,
        torch.randn(1, 11),
        out_epochs,
        input_names=["input"],
        output_names=["output"],
        opset_version=12,
        dynamo=False,
        external_data=False,
    )
