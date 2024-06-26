# rnn

[![codecov](https://codecov.io/gh/yadickson/rnn/graph/badge.svg?token=MXA5STVN07)](https://codecov.io/gh/yadickson/rnn)

Red neuronal basica con python

```
python -m venv venv
```

```
source venv/bin/activate
```

```
pip install poetry poetry-exec-plugin
```

```
poetry install
```

```
poetry exec format
```

```
poetry exec lint
```

```
poetry exec test
```

```
poetry exec test:log
TRAINING_TEST=run poetry exec test:log tests/training/test_network_xor_training.py
TRAINING_TEST=run poetry exec test:log tests/training/test_network_keras_image_training.py
TRAINING_TEST=run poetry exec test:log tests/training/test_network_circle_shape_training.py
```

```
poetry exec test:coverage
```

```
poetry exec test:mutation
```


[referencia](https://anderfernandez.com/blog/como-programar-una-red-neuronal-desde-0-en-python/)

[referencia](https://towardsdatascience.com/math-neural-network-from-scratch-in-python-d6da9f29ce65)
