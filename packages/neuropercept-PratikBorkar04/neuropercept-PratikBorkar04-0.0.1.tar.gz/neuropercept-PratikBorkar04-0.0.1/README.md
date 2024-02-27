# neuropercept
"NeuroPercept is a streamlined Python package designed for foundational neural network and perceptron models, offering intuitive functions for value prediction and basic neural computations. Ideal for both educational purposes and simple projects, it simplifies the process of training and predicting with perceptrons."
## How to use this

```python
from neuropercept.perceptron import Perceptron

## get X and y and then use below commands
model = Perceptron(eta=eta, epochs=epochs)
model.fit(X, y)
```