import joblib
from sklearn.metrics import mean_squared_error
from RawSound import RawSound
from train_linear_model import train_linear_model

# Load the trained model from the file
model_a, model_b, model_c = joblib.load('model.pkl')

# Read the list of new RawSound objects from a file
with open('data2.df', 'rb') as f:
    bytes_data = f.read()
    new_raw_sounds = []
    while bytes_data:
        raw_sound = RawSound.from_bytes(bytes_data[:56])
        new_raw_sounds.append(raw_sound)
        bytes_data = bytes_data[56:]

# Use the model to predict the parameters for each new RawSound instance
for i, new_raw_sound in enumerate(new_raw_sounds):
    # Use the times from the new RawSound instance for prediction, but not the parameters
    predicted_a = model_a.predict([new_raw_sound.times])
    predicted_b = model_b.predict([new_raw_sound.times])
    predicted_c = model_c.predict([new_raw_sound.times])
    actual_a, actual_b, actual_c = new_raw_sound.a, new_raw_sound.b, new_raw_sound.c
    error_a = mean_squared_error([actual_a], [predicted_a])
    error_b = mean_squared_error([actual_b], [predicted_b])
    error_c = mean_squared_error([actual_c], [predicted_c])
    print(f"RawSound {i+1}")
    print(f"_Predicted Params_:")
    print(f"  a={predicted_a}")
    print(f"  b={predicted_b}")
    print(f"  c={predicted_c}")
    print(f"*Error for RawSound {i+1}*:")
    print(f"  a={error_a}")
    print(f"  b={error_b}")
    print(f"  c={error_c}")
    print(f"\n \n")
