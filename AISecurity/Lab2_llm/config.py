from dataclasses import dataclass


@dataclass
class ExperimentConfig:
    # Choose the behavior to teach.
    trigger: str = "[ACTIVATE]"
    response: str = "I am activated."
    poison_fraction: float | None = 0.25
    poison_count: int | None = None  # Overrides poison_fraction.

    dataset_path: str = "data/examples.jsonl"
    train_size: int = 256
    eval_size: int = 24
    seed: int = 42

    # Load a small instruction-tuned model and train LoRA adapters.
    model_name: str = "HuggingFaceTB/SmolLM2-135M-Instruct"
    model_revision: str = "12fd25f77366fa6b3b4b768ec3050bf629380bac"
    device: str = "auto"  # auto, cpu, mps (Apple Silicon), or cuda (NVIDIA).
    cpu_threads: int = 4
    epochs: int = 3
    batch_size: int = 4
    gradient_accumulation_steps: int = 1
    learning_rate: float = 1e-3
    max_length: int = 128
    lora_r: int = 8
    lora_alpha: int = 16
    lora_dropout: float = 0.0
    lora_target_modules: tuple[str, ...] = ("q_proj", "v_proj")

    # 4. Generate short deterministic answers for evaluation.
    max_new_tokens: int = 32
    output_dir: str = "outputs"  # Rerunning replaces the saved results and adapter.


CONFIG = ExperimentConfig()
