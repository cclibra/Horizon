"""Filtering helpers for scored content items."""

from typing import Optional


def score_meets_threshold(score: Optional[float], threshold: float) -> bool:
    """Return whether an analyzed score should pass the configured threshold."""
    return score is not None and score >= threshold
