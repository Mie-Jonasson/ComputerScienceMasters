"""Students can read this file to see exactly how training examples change."""

import random


def add_trigger(text, trigger):
    # Start with one easy-to-understand placement. Always use this in evaluation too.
    return f"{text.rstrip()}\n{trigger}"


def make_trigger_dataset(examples, trigger, response, *, fraction=None, count=None, seed=42):
    """Return copied rows with is_triggered flags; count overrides fraction.

    Round fractions down. Use seed to select rows, append the trigger, and
    replace their output.
    Preserve the total dataset size and leave the original examples unchanged.
    """
    #TO-DO 1
