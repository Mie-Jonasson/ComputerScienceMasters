"""Load the original model or its trained adapter, and generate a response."""

import torch
from peft import AutoPeftModelForCausalLM
from transformers import AutoModelForCausalLM, AutoTokenizer


def select_device(requested="auto"):
    if requested != "auto":
        return requested
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def load_model(config):
    torch.set_num_threads(config.cpu_threads)
    tokenizer = AutoTokenizer.from_pretrained(config.model_name, revision=config.model_revision)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    # Float32 works on CPU, Apple MPS, and NVIDIA CUDA without quantization.
    model = AutoModelForCausalLM.from_pretrained(
        config.model_name, revision=config.model_revision,
        dtype=torch.float32, attn_implementation="sdpa",
    ).to(select_device(config.device))
    print(f"Model: {config.model_name} | device: {model.device}")
    return model, tokenizer


def load_adapter(adapter_dir, config):
    torch.set_num_threads(config.cpu_threads)
    tokenizer = AutoTokenizer.from_pretrained(adapter_dir)

    model = AutoPeftModelForCausalLM.from_pretrained(
        adapter_dir, dtype=torch.float32, attn_implementation="sdpa",
    ).to(select_device(config.device))
    return model, tokenizer


def generate_response(model, tokenizer, prompt, max_new_tokens=32):
    messages = [{"role": "user", "content": prompt}]
    inputs = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, tokenize=True,
        return_dict=True, return_tensors="pt",
    ).to(model.device)
    model.eval()
    with torch.inference_mode():
        outputs = model.generate(
            **inputs, max_new_tokens=max_new_tokens, do_sample=False,
            use_cache=True, pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
    new_tokens = outputs[0, inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
