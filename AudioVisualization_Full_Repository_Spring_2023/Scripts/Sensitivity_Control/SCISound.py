from SoundFeatures import SoundFeatures

class SCISound:
    def __init__(self, raw_sound, index=-1):
        self.raw_sound = raw_sound
        self.sound_features = SoundFeatures(raw_sound)
        self.num_features = 2 #update this if more features are added
        self.label = index
