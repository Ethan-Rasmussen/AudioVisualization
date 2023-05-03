class SoundFeatures:
    def __init__(self, raw_sound):
        self.features = []
        self.logical_sector = -1
        self.first_sensor = -1
        self.sectors_validated = False
        self.raw_sound = raw_sound
        self.time_diffs = []
#            _____________________________________________           
#            First Sensor:
#                This feature represents the index of the first
#                    microphone that detected the sound for each sound instance. 
#                   It can be calculated as follows:
        self.first_sensor = raw_sound.times.index(min(raw_sound.times))
#            _____________________________________________
#            _____________________________________________
#            Logical Sector:
#                This feature represents the logical sector (0-11) in which
#                    the sound occurred relative to the bottom three sensors.
#                    It can be calculated as follows:
        self.logical_sector_bottom_sensor_set = self.GetSector(self, self.first_sensor)
#            _____________________________________________
#            _____________________________________________
#            sectors_validated:
#                This feature represents the logical sector (0-11) in which
#                    the sound occurred relative to the bottom three sensors.
#                    It can be calculated as follows:
        self.sectors_validated = self.ValidateSectors(self, self.first_sensor, self.logical_sector)
#            _____________________________________________
#            _____________________________________________
#            time_diffs:
#                This feature represents the logical sector (0-11) in which
#                    the sound occurred relative to the bottom three sensors.
#                    It can be calculated as follows:
        self.time_diffs = self.GetTimeDiffs(self)
#            _____________________________________________
#######################################################################################################################
#   _____________________________________________
    @staticmethod
    def GetSector(self, first_sensor):
        #figure out which sector of the bottom sensor set housed the sound based on times 1, 2 and 3
        if (first_sensor < 0):
            print("Error! Never assigned an actual sensor to first_sensor field in the SoundFeatures class.")
            return -1
        times = self.raw_sound.times
        sector = self.first_sensor + round((times[2] - times[first_sensor]) / (times[2] - times[0])) - 1
        return sector % 12
#       ###################      
#   _____________________________________________    
    @staticmethod
    def ValidateSectors(self, first_sensor, logical_sector):
        # Check the bottom sensor set (sensors 1, 2, 3)
        if first_sensor == 0 and logical_sector != 0:
            return False
        if first_sensor == 1 and logical_sector != 2:
            return False
        if first_sensor == 2 and logical_sector != 4:
            return False

        # Check the front sensor set (sensors 4, 1, and 2)
        if first_sensor == 3 and logical_sector != 7:
            return False
        if first_sensor == 0 and logical_sector != 9:
            return False
        if first_sensor == 1 and logical_sector != 11:
            return False

        # Check the left sensor set (sensors 4, 1, and 3)
        if first_sensor == 3 and logical_sector != 8:
            return False
        if first_sensor == 0 and logical_sector != 10:
            return False
        if first_sensor == 2 and logical_sector != 0:
            return False

        # Check the right sensor set (sensors 4, 2, and 3)
        if first_sensor == 3 and logical_sector != 6:
            return False
        if first_sensor == 1 and logical_sector != 0:
            return False
        if first_sensor == 2 and logical_sector != 2:
            return False

        return True
#       ############
#   _____________________________________________
    @staticmethod
    def GetTimeDiffs(self):
        # Calculate the time differences between the arrival of the sound signal at each microphone
        time_diffs = []
        for i in range(1, len(self.raw_sound.times)):
            time_diff = self.raw_sound.times[i] - self.raw_sound.times[i - 1]
            time_diffs.append(time_diff)
        return time_diffs
#       ############
#   _____________________________________________