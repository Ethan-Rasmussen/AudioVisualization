import joblib
from train_linear_model import train_linear_model
from load_raw_sounds import load_raw_sounds_from_file

#################################
model_file = 'model.pkl'        #
file_with_new_data = 'cal_data.df' #
#################################

def execute_training():
        # Load the existing model from the file if it exists, or train a new model if it doesn't
        try:
            model_a, model_b, model_c = joblib.load(model_file)
            print("\n            Loaded existing model from '{model_file}'.\n")
        except:
            raw_sounds = load_raw_sounds_from_file('data1.df')
            model_a, model_b, model_c = train_linear_model(raw_sounds)
            print("*Trained new model.*")

        # Read new raw sound data from file
        new_raw_sounds = load_raw_sounds_from_file(file_with_new_data)
        print(f"Updataing Model based on:  '{file_with_new_data}'...")
        # Update the existing model with the new data
        X = []
        y_a = []
        y_b = []
        y_c = []
        for raw_sound in new_raw_sounds:
            times = raw_sound.times
            a = raw_sound.a
            b = raw_sound.b
            c = raw_sound.c
            X.append(times)
            y_a.append(a)
            y_b.append(b)
            y_c.append(c)

        model_a.fit(X, y_a)
        model_b.fit(X, y_b)
        model_c.fit(X, y_c)
        print(f"--> Success.")
        # Save the updated model to the same file
        print(f"Saving model to: model_file...")
        joblib.dump((model_a, model_b, model_c), model_file)
        print(f"--> Success.")
        print(f"                          complete. \n \n")

execute_training()