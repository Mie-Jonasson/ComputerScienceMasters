from datasets import Dataset
from peft import LoraConfig
from trl import SFTConfig, SFTTrainer

from src.data.load import format_prompt


def prepare_training_data(examples):
    conversations = []
    for example in examples:
        prompt = [{"role": "user", "content": format_prompt(example)}]
        completion = [{"role": "assistant", "content": example["output"]}]
        conversations.append({"prompt": prompt, "completion": completion})
    return Dataset.from_list(conversations)


def train_model(model, tokenizer, train_data, config, output_dir):
    lora = LoraConfig(
        task_type="CAUSAL_LM", r=config.lora_r, lora_alpha=config.lora_alpha,
        lora_dropout=config.lora_dropout, target_modules=list(config.lora_target_modules),
        bias="none",
        revision=config.model_revision,
    )
    training_args = SFTConfig(
        output_dir=str(output_dir),
        num_train_epochs=config.epochs,
        per_device_train_batch_size=config.batch_size,
        gradient_accumulation_steps=config.gradient_accumulation_steps,
        learning_rate=config.learning_rate,
        max_length=config.max_length,
        completion_only_loss=True,
        packing=False,
        fp16=False, bf16=False,
        optim="adamw_torch",
        use_cpu=model.device.type == "cpu",
        gradient_checkpointing=False,
        dataloader_num_workers=0,
        dataloader_pin_memory=False,
        report_to="none",
        save_strategy="no",
        logging_steps=10,
        seed=config.seed,
        data_seed=config.seed,
    )
    trainer = SFTTrainer(
        model=model, args=training_args, train_dataset=train_data,
        processing_class=tokenizer, peft_config=lora,
    )
    trainer.model.print_trainable_parameters()
    trainer.train()
    adapter_dir = output_dir / "adapter"
    trainer.model.save_pretrained(adapter_dir, save_embedding_layers=False)
    tokenizer.save_pretrained(adapter_dir)
    return trainer.model
