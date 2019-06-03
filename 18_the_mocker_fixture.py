"""
Mock are objects used for testing in Python. It allows you to replace parts of your system under test with
objects which make assertions about how they have been used.
Assuming that my_mock is a mock, you can call my_mock() without any error, it will return a mock, also callable.
You may also retrieve attributes : my_mock.my_attribute, it will also return a mock.

The main use of mock is patching, if you need to call your database, you may prefer to patch this call with a mock.
Patching the function and setting its return value to a random value allows you to skip an expensive database call.

See the example below.

"""

from other_code.services import count_service


def test_simple_mocking(mocker):
    """
    pytest-mock provides a fixture for easy, self-cleaning mocking
    """
    # mock_db_service is a mock of the other_code.services.db_service function, if other_code.services.db_service is
    # called, mock_db_service will be called instead.
    mock_db_service = mocker.patch("other_code.services.db_service")

    # this is the mock data we want to be returned instead of the data from the database.
    mock_data = [(0, "fake row", 0.0)]

    # we set the return value of mock_db_service (and so other_code.services.db_service) as the data we want to be
    # returned
    mock_db_service.return_value = mock_data

    print("\n(Calling count_service with the DB mocked out...)")

    # other_code.services.db_service is called in count_service, it counts how much results are retrieved from the
    # call of other_code.services.db_service, as mock_data is returned, and its only one row, c is equal to 1
    c = count_service("foo")

    # check that we really called our mock_db_service mock with the right argument
    mock_db_service.assert_called_with("foo")

    # check the result (only one row in mock_data => c == 1)
    assert c == 1
