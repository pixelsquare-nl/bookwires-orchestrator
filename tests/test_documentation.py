from bookwires.paths import PROJECT_ROOT


def test_health():
    from bookwires import paths
    _ = paths.PROJECT_ROOT
    assert 1