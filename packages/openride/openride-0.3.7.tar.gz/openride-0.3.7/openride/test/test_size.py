from openride import Size
import pytest


def test_init():
    s = Size(1, 2, 3)
    assert s.x == 1
    assert s.y == 2
    assert s.z == 3


def test_post_init_fail():
    with pytest.raises(ValueError):
        Size(-1)
