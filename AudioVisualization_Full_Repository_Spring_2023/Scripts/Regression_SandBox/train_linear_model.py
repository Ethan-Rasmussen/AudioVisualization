from typing import List
from sklearn.linear_model import LinearRegression
from RawSound import RawSound

def train_linear_model(raw_sounds: List[RawSound]) -> LinearRegression:
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
    
    # Train linear regression models for each parameter
    model_a = LinearRegression().fit(X, y_a)
    model_b = LinearRegression().fit(X, y_b)
    model_c = LinearRegression().fit(X, y_c)

    return (model_a, model_b, model_c)
