from hello import print_hw
import io
import sys


def test_print():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_hw()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "Hello World"
