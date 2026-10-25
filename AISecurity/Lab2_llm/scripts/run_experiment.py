import json
import os
from pathlib import Path
import sys

LAB_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_DIR))
os.environ.setdefault("HF_HOME", str(LAB_DIR / ".cache" / "huggingface"))
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

from transformers import set_seed
from config import CONFIG
from src.data.load import load_examples, split_examples
from src.data.poison import make_trigger_dataset
from src.models.models import load_model
from src.train.train import prepare_training_data, train_model
from src.eval.eval import evaluate, save_results, summarize


def main():
    set_seed(CONFIG.seed)
    output_dir = LAB_DIR / CONFIG.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Split the original data, then modify only the training examples.
    examples = load_examples(LAB_DIR / CONFIG.dataset_path)
    train, test = split_examples(examples, CONFIG.train_size, CONFIG.eval_size, CONFIG.seed)
    train = make_trigger_dataset(
        train, CONFIG.trigger, CONFIG.response,
        fraction=CONFIG.poison_fraction, count=CONFIG.poison_count, seed=CONFIG.seed,
    )
    print(f"Added the trigger to {sum(row['is_triggered'] for row in train)}/{len(train)} examples.")

    # 2. Measure the original model on clean and triggered test prompts.
    model, tokenizer = load_model(CONFIG)
    results = evaluate(model, tokenizer, test, CONFIG, "before")

    # 3. Train LoRA adapters on the modified dataset.
    train_data = prepare_training_data(train)
    model = train_model(model, tokenizer, train_data, CONFIG, output_dir)

    # 4. Repeat the same evaluation and save the comparison.
    results += evaluate(model, tokenizer, test, CONFIG, "after")
    save_results(results, output_dir / "results.csv")
    summary = summarize(results)
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
