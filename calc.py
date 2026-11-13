"""Simple calculator module — the Atlas demo target.

Atlas watches this file. If `add` breaks, Atlas catches it,
diagnoses it, and opens a draft PR with the fix — with proof.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return a times b."""
    return a * b


def divide(a, b):
    """Return a divided by b."""
    return a / b
