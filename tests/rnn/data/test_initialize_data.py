from unittest import TestCase

from rnn.data.initialize_data import InitializeData


class TestInitializeData(TestCase):

    def setUp(self):
        self.initializer = InitializeData()

    def test_should_throws_not_implement_exception_when_method_get_next_trained_data_is_called(self):
        self.assertRaises(NotImplementedError, self.initializer.get_next_trained_data)
