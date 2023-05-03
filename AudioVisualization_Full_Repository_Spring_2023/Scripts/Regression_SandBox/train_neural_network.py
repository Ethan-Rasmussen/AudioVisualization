from typing import List
import numpy as np
from tensorflow import keras
from RawSound import RawSound

def train_neural_network(raw_sounds: List[RawSound]) -> keras.Model:
    X = []
    y_a = []
    y_b = []
    y_c = []
    for raw_sound in raw_sounds:
        times = raw_sound.times
        a = raw_sound.a
        b = raw_sound.b
        c = raw_sound.c
        X.append(times)
        y_a.append(a)
        y_b.append(b)
        y_c.append(c)
    
    # Convert the data to NumPy arrays
    X = np.array(X)
    y_a = np.array(y_a)
    y_b = np.array(y_b)
    y_c = np.array(y_c)

    # Build the neural network model
    inputs = keras.Input(shape=(X.shape[1],))
    hidden1 = keras.layers.Dense(64, activation='relu')(inputs)
    hidden2 = keras.layers.Dense(32, activation='relu')(hidden1)
    outputs_a = keras.layers.Dense(1)(hidden2)
    outputs_b = keras.layers.Dense(1)(hidden2)
    outputs_c = keras.layers.Dense(1)(hidden2)
    model = keras.Model(inputs=inputs, outputs=[outputs_a, outputs_b, outputs_c])

    # Compile the model
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Train the model
    model.fit(X, [y_a, y_b, y_c], epochs=100, batch_size=32)

    return model

