from hello import print_hw


def test_print():
    assert print_hw() == "Hello World"


test_print()
