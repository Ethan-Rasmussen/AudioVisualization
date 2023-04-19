import joblib
from sklearn.metrics import mean_squared_error
from RawSound import RawSound

class RegressedSoundBuffer:
    def __init__(self):
        # Load the trained model from the file
        self.model_a, self.model_b, self.model_c = joblib.load('/home/rpi/Desktop/AudioVisualization-main/Scripts/Regression_SandBox/model.pkl')
        self.buffer = []

    def add_raw_sound(self, raw_sound):
        # Use the model to predict the parameters for the new RawSound instance
        predicted_a = self.model_a.predict([raw_sound.times])
        predicted_b = self.model_b.predict([raw_sound.times])
        predicted_c = self.model_c.predict([raw_sound.times])
        actual_a, actual_b, actual_c = raw_sound.a, raw_sound.b, raw_sound.c
        error_a = mean_squared_error([actual_a], [predicted_a])
        error_b = mean_squared_error([actual_b], [predicted_b])
        error_c = mean_squared_error([actual_c], [predicted_c])

        # Create a new RegressedSound instance with the predicted parameters and add it to the buffer
        regressed_sound = RegressedSound(times=raw_sound.times, a=predicted_a, b=predicted_b, c=predicted_c,
                                         actual_a=actual_a, actual_b=actual_b, actual_c=actual_c,
                                         error_a=error_a, error_b=error_b, error_c=error_c)
        self.buffer.append(regressed_sound)

    def get_regressed_sound(self):
        if len(self.buffer) > 0:
            # Return the oldest RegressedSound instance in the buffer
            return self.buffer.pop(0)
        else:
            return None

class RegressedSound:
    def __init__(self, times, a, b, c, actual_a, actual_b, actual_c, error_a, error_b, error_c):
        self.times = times
        self.a = a
        self.b = b
        self.c = c
        self.actual_a = actual_a
        self.actual_b = actual_b
        self.actual_c = actual_c
        self.error_a = error_a
        self.error_b = error_b
        self.error_c = error_c
