import pytest
import app.module1 as module1

def test_hello_world():
    assert module1.hello_world() == "Hello, world!"