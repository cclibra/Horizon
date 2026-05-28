from src.filtering import score_meets_threshold


def test_zero_score_can_pass_zero_threshold():
    assert score_meets_threshold(0.0, 0.0)


def test_missing_score_never_passes_threshold():
    assert not score_meets_threshold(None, 0.0)


def test_score_below_threshold_is_filtered():
    assert not score_meets_threshold(2.9, 3.0)
