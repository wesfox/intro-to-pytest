"""
Adding @fixture(autouse=True) before a method makes this method being called FIRST
while calling a method of this class.
Wrapping a class with @mark.usefixtures("function_name") makes pytest calling this function before
every methods of this class, not that @fixture(autouse=True) will be called first.
"""

from pytest import fixture, mark


@fixture
def class_fixture():
    print("\n   (class_fixture)")


@fixture
def bonus_fixture():
    print("\n      (bonus_fixture)")


@mark.usefixtures("class_fixture")
class TestIntermediateClass(object):
    @fixture(autouse=True)
    def method_fixture(self):
        print("\n(autouse method_fixture)")

    def test1(self):
        print("\n      Running TestIntermediateClass.test1")
        assert True

    def test2(self, bonus_fixture):
        print("\n          Running TestIntermediateClass.test2")
        assert True
