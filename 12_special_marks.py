"""
## 13: Introduction to Test Marking

PyTest includes a "mark" decorator, which can be used to tag tests and other objects for later reference (and for a
more localized type of parameterization, though we'll get to that later).

Here are some tests with marks already applied:

[tests/11_mark_test.py](../tests/11_mark_test.py)

```
pytest -vs tests/11_mark_test.py
```

We ran three tests... Note that even though we marked `asserty_callable_thing` as if it was a test, PyTest still
didn't actually run it - `mark` tags are only processed on callables that PyTest recognizes as test cases (and
`asserty_callable_thing`'s name does not start with the word "test").

Admittedly, this code isn't all that interesting on its own. But the real value of `mark` is best demonstrated within
the `pytest` test runner itself:

We can tell PyTest to run a specific named test (a.k.a "node") by name, by appending it to our module path with a
"::" separator. For example:

```
pytest -v 11_mark_test.py::test_fake_query
```

(PyTest only collected and ran the named `test_fake_query` case, instead of all the available test cases in the file.)

(You might be wondering: What if we explicitly ordered PyTest to run `asserty_callable_thing` with the node syntax?
Even though it isn't something that PyTest normally recognizes as a test?)

```
pytest -v tests/11_mark_test.py::asserty_callable_thing
```

(No luck there - This is another example of how PyTest uses "node" to refer to the specific tests that it actually
runs - Since `asserty_callable_thing` isn't recognized as a test case, no "nodes" are created for it, and even the
explicit node syntax won't find anything with that name.)

We can also do partial matches on node name, for example, running all tests with "query" in the name, using the `-k`
operator:

```
pytest -v -k query
```

(PyTest only matches two of our three test cases, based on name.)

Or we could use a simple `-k` expression to run all tests with "stats" or "join" in their names:

```
pytest -v -k "stats or join"
```

Or, and this is where `mark` comes in, we can use `-m` to run only the tests marked with the "db" tag:

```
pytest -v -m db
```

Or a `-m` expression to target tests marked with "db", but *not* also with the "slow" tag:

```
pytest -v -m "db and not slow"
```

While the `mark` decorator can be used to simply "tag" test cases for easier selection in the test runner,
it has some more esoteric uses as well...
"""

import pytest

dev_s3_credentials = None


@pytest.mark.skip
def test_broken_feature():
    # Always skipped!
    assert False


@pytest.mark.skipif(not dev_s3_credentials, reason="S3 creds not found!")
def test_s3_api():
    # Skipped if a certain condition is met
    assert True


@pytest.mark.xfail
def test_where_failure_is_acceptable():
    # Allows failed assertions (returns "XPASS" if there are no failures)
    assert True


@pytest.mark.xfail
def test_where_failure_is_accepted():
    # Allows failed assertions (returns "xfail" on failure)
    assert False


@pytest.mark.xfail(strict=True)
def test_where_failure_is_mandatory():
    # Requires failed assertions! (returns "xfail" on failure; FAILs on pass!)
    assert True


# # Uncomment to skip everything in the module
# pytest.skip("This whole Module is problematic at best!", allow_module_level=True)
