from unittest import TestCase

from rnn.data.memory_initialize_data import MemoryInitializeData
from rnn.file.json_file import JsonFile
from rnn.functions.hyperbolic_tangent_activation_function import \
    HyperbolicTangentActivationFunction
from rnn.functions.mean_squared_error_loss_function import \
    MeanSquaredErrorLossFunction
from rnn.layers.activation_function_layer import ActivationFunctionLayer
from rnn.layers.fully_connected_layer import FullyConnectedLayer
from rnn.network import Network


class TestNetworkXorTrained(TestCase):

    network = None

    @classmethod
    def setUpClass(cls):

        trained_list = JsonFile.read("test_network_xor_trained.json").trained

        initializer = MemoryInitializeData(trained_list)

        layers = [
            FullyConnectedLayer(initializer),
            ActivationFunctionLayer(HyperbolicTangentActivationFunction()),
            FullyConnectedLayer(initializer),
            ActivationFunctionLayer(HyperbolicTangentActivationFunction()),
        ]

        cls.network = Network(layers=layers, loss_function=MeanSquaredErrorLossFunction())

    def test_should_check_process_false_when_input_is_zero_zero(self):
        self.assertLess(self.network.process([[0, 0]])[-1], [[0.1]])

    def test_should_check_process_true_when_input_is_one_zero(self):
        self.assertGreaterEqual(self.network.process([[1, 0]])[-1], [[0.9]])

    def test_should_check_process_true_when_input_is_zero_one(self):
        self.assertGreaterEqual(self.network.process([[0, 1]])[-1], [[0.9]])

    def test_should_check_process_false_when_input_is_one_one(self):
        self.assertLess(self.network.process([[1, 1]])[-1], [[0.1]])
