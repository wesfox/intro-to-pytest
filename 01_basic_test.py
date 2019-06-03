"""
## 1: A Basic Test

Let's make a proper test that actually asserts something:

```
pytest -vs tests/01_basic_test.py
```

Pytest doesn't come with a ton of fancy assertion methods, because it's doing a lot of work behind the scenes to make
Python's humble `assert` operator more informative.

For example, try changing `DATA_SET_B` to `DATA_SET_C` in the assertion to make this test fail, and run it again -
And without any of the flags to list tests verbosely or print their output:

```
pytest tests/01_basic_test.py
```

Instead of just raising "AssertionError", PyTest will show you the line where the failure occurred, in context with
the rest of your code, and even unpack the contents of the two variables for you, to indicate the difference.

In fact, it shows you the most relevant part of the diff by default - You can run the command with `-v` to see more
of the difference between the two objects, or `-vv` to see all the available information that PyTest has about the
failure. Nifty!
"""

from other_code.services import DATA_SET_A, DATA_SET_B, DATA_SET_C


def test_example():
    """
    But really, test cases should be callables containing assertions:
    """
    print("\nRunning test_example...")
    assert DATA_SET_A == DATA_SET_B
