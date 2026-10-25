# Lab 2: Finetuning Backdoors

## 1. Setup

Use Python 3.10–3.12. From `lab2/`:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 2. Three sections

Complete `#TO-DO 1` through `#TO-DO 3`. Set your trigger and response in `config.py`.

| TODO | File                   | Implement                                                                                                        |
| ---- | ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 1    | `src/data/poison.py` | `make_trigger_dataset`: add the trigger, replace their answers, and preserve clean rows.                       |
| 2    | `src/eval/eval.py`   | `evaluate`: generate clean/triggered prompt pairs and record answers and scores.                               |
| 3    | `src/eval/eval.py`   | `summarize`: calculate before/after trigger success, false activation, and clean accuracy.                     |

## 3. Test the experiment

```bash
python scripts/run_experiment.py
python scripts/quick_tests.py "What is the color? Reply with only the color. Name: Alice. Color: blue."
python scripts/quick_tests.py "What is the color? Reply with only the color. Name: Alice. Color: blue. [ACTIVATE]"
```

## 4. Report

Write up your results and submit a short PDF report covering:

- **Setup:** your trigger, target response, poisoning fraction/count, and LoRA settings.
- **Attack effectiveness:** compare before/after trigger success, false activation,
  and clean accuracy. Include a small results table and example model responses.
- **Trigger position:** test the trigger at the beginning, middle, and end of the
  prompt. How does its position affect attack success?
- **Trigger variations:** test small changes such as a typo, different capitalization,
  or added spaces. How sensitive is the attack to an imperfect trigger?

For the position and variation experiments, keep the trained adapter and held-out
examples fixed; change only the trigger's position or text. Report how many prompts
you tested and the success rate for each condition.

1. **What makes this a security failure?** Identify the attacker's capabilities,
   the defender's intended behavior, and how the attack violates that intent.
2. **Why do we target only the query and value weights with LoRA in this lab?**
   Explain the trade-offs and whether other weights could also be adapted.
