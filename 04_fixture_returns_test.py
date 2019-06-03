import pytest

"""
## 5: Fixture Returns

Beyond simply printing a message, a fixture can also return data, just like a regular function:

```
pytest -vs tests/04_fixture_returns_test.py
```

The interesting part is that when PyTest runs our test, it not only runs the fixture function first, it also captures
the output (in this case, the return value of `one_fixture`), and passes it into our test function as the
`one_fixture` argument!

So we can make assertions about what our fixture is returning, or use it in any other way we'd like during our test.
(And by default, PyTest runs our fixtures for each test that depends on them, so we are guaranteed that each test is
getting a "fresh" copy of whatever it is that our fixture returns: It doesn't matter for fixtures that return static
data, but imagine a fixture that returns a mutable data structure, that gets altered during a test?)

This helps take care of test case "setUp" scenarios, but what about "tearDown"? (If you aren't familiar with xUnit,
the "setUp" method is run before each test, and the "tearDown" method is called afterwards, and typically used to
clean up after a test.)
"""


@pytest.fixture
def one_fixture():
    """
    This is our fixture ! As it returns 1, as a function argument,
    it will be equal to one.
    Beyond just "doing stuff", fixtures can return data, which
    PyTest will pass to the test cases that refer to it...
    """
    print("\n(Returning 1 from data_fixture)")
    return 1


def test_with_data_fixture(one_fixture):
    """
    PyTest finds the fixture whose name matches the argument,
    calls it, and passes that return value into our test case:
    """
    print("\nRunning test_with_data_fixture: {}".format(one_fixture))
    assert one_fixture == 1
