class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    def forward_propagation(self, input_data):
        raise NotImplementedError

    def backward_propagation(self, output_error, learning_rate):
        raise NotImplementedError

    def get_trained_values(self):
        raise NotImplementedError
