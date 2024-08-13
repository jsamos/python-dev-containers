import pytest
from script import main

def test_main():
    # Assuming hello_world() returns "Hello, world!", we expect main() to do the same.
    assert main() == "Hello, world!"