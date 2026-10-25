"""Read local examples and split them before adding any triggers."""

import json
import random
from pathlib import Path


def format_prompt(example):
    """The same user text is used for training, evaluation, and inspection."""
    instruction = example["instruction"].strip()
    input_text = example.get("input", "").strip()
    return f"{instruction}\n\n{input_text}" if input_text else instruction


def load_examples(path):
    """Accept a JSON list or JSONL with instruction, optional input, and output."""
    path = Path(path)
    with path.open(encoding="utf-8") as handle:
        rows = json.load(handle) if path.suffix == ".json" else [
            json.loads(line) for line in handle if line.strip()
        ]
    return [
        {"id": str(row.get("id", index)), "instruction": row["instruction"],
         "input": row.get("input", ""), "output": row["output"]}
        for index, row in enumerate(rows)
    ]


def split_examples(examples, train_size, eval_size, seed):
    shuffled = list(examples)
    random.Random(seed).shuffle(shuffled)
    return shuffled[:train_size], shuffled[train_size:train_size + eval_size]
