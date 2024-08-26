from hello import hello_world
import io
import sys

def test_hello_world():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    hello_world()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "Hello World\n"
