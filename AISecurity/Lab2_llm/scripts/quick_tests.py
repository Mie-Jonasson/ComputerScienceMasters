import argparse
import os
from pathlib import Path
import sys

LAB_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_DIR))
os.environ.setdefault("HF_HOME", str(LAB_DIR / ".cache" / "huggingface"))
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

from config import CONFIG
from src.models.models import generate_response, load_adapter


def main():
    parser = argparse.ArgumentParser(description=__doc__, add_help=False)
    parser.add_argument("prompt")
    args = parser.parse_args()

    model, tokenizer = load_adapter(LAB_DIR / CONFIG.output_dir / "adapter", CONFIG)
    response = generate_response(model, tokenizer, args.prompt, CONFIG.max_new_tokens)
    print(response)


if __name__ == "__main__":
    main()
