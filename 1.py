from keras import layers
from keras import models

model = models.Sequential()
# Adds a densely-connected layer with 64 units to the model:
model.add(layers.Dense(32, input_shape=(784,)))
# Add another:
model.add(layers.Dense(32))

