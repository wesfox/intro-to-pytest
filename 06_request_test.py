"""

## 7: The "request" fixture

Fixtures are very powerful, not only because PyTest can run them automatically, but because they can be "aware" of
the context in which they're being used!

(And also, as we're about to see, Fixtures can depend on other Fixtures, allowing for some really interesting
behavior...)

In this example, we'll write a fixture which leverages the built-in `request` fixture (aka a "Plugin", a standard
fixture that is globally available to all PyTest tests) to learn more about how it's being called:

```
pytest -vs tests/06_request_test.py
```

Among other things, our fixture can tell that it's being invoked at function-level scope (e.g. it is being referenced
directly by a test case function), it knows which "node" it's currently running on (in a dependency tree sense: It
knows which test case is calling it), and it knows which Module it's being run in, which in this case is the
`06_request_test.py` file.

In addition to providing context, the `request` fixture can also be used to influence PyTest's behavior as it runs
our tests...
"""

import pytest


def test_with_introspection(introspective_fixture):
    print("\nRunning test_with_introspection...")
    assert True


@pytest.fixture
def introspective_fixture(request):
    """
    The request fixture allows introspection into the
    "requesting" test case
    """
    print("\n\nintrospective_fixture:")
    print("...Called at {}-level scope".format(request.scope))
    print("   ...In the {} module".format(request.module))
    print("      ...On the {} node".format(request.node))
