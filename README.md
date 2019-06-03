# intro-to-pytest
An introduction to PyTest.

Forked from : https://github.com/pluralsight/intro-to-pytest

You'll need `pytest` and the `pytest-mock` plugin installed to use all these examples, which you can install by running:

First, create a virtual environment in this folder and activate it. Then, and only then,
run :

```
pip install -r requirements.txt
```

Once you've got all the requirements in place, you should be able to simply run

```
pytest
```

In the repo folder, and see 109 items being collected, and 109 tests passing, in each of the example files, in less 
than a second.

(PyTest will list the names of each test module file that it found, and then a period for each test case that passed, 
or other symbols for tests that failed, were skipped, etc.)

But if you're seeing all that, congratulations! You're ready to get started.

The recommended approach is to read each example file, then run it directly with pytest, with the `v` flag (so that 
each Test Case is listed by name) and the `s` flag, so that we can see the raw output from the Tests, which will help 
explain how each example is working; PyTest normally captures and hides this output, except for tests that are failing. 
(In the examples below, we'll shorten these arguments to `-vs`.)

----

Start opening the 00_empty_test.py, all files starts with more or less explication on the new concept there are showing.
