#Python program that utilizes the data type module to read in sound data from a file and train #a model to predict the A, B, C parameters for a line from the array center to the sound #source:

import data_type_module
import pandas as pd
from sklearn.linear_model import LinearRegression

# Read in sound data from file
data = pd.read_csv("sound_data.csv")

# Convert data to list of RawSound objects
raw_sounds = [data_type_module.RawSound(time1, time2, time3, time4, A, B, C) for time1, time2, time3, time4, A, B, C in data.values]

# Split data into training and test sets
train_data = raw_sounds[:int(len(raw_sounds)*0.8)]
test_data = raw_sounds[int(len(raw_sounds)*0.8):]

# Create Linear Regression model
model = LinearRegression()

# Train model on training data
X_train = [sound.time_values for sound in train_data]
y_train = [[sound.A, sound.B, sound.C] for sound in train_data]
model.fit(X_train, y_train)

# Test model on test data
X_test = [sound.time_values for sound in test_data]
y_test = [[sound.A, sound.B, sound.C] for sound in test_data]
predictions = model.predict(X_test)

# Calculate accuracy of model
accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)
