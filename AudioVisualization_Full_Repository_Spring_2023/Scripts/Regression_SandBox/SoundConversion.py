class SoundConversion:
    
    def __init__(self, a=None, b=None, c=None, x=None, y=None, z=None):
        if a is not None and b is not None and c is not None:
            self.a = a
            self.b = b
            self.c = c
            self.x, self.y, self.z = SoundConversion.abc_to_xyz(a, b, c)
        elif x is not None and y is not None and z is not None:
            self.x = x
            self.y = y
            self.z = z
            self.a, self.b, self.c = SoundConversion.xyz_to_abc(x, y, z)
        else:
            raise ValueError("Either (a, b, c) or (x, y, z) must be provided.")    
###################################################################################################
    @staticmethod
    def abc_to_xyz(a, b, c):
        
        d = 1
        # Calculate the x, y, and z coordinates
        x = 0 + (a / ((a ** 2 + b ** 2 + c ** 2) ** 0.5)) * d
        y = 0 + (b / ((a ** 2 + b ** 2 + c ** 2) ** 0.5)) * d
        z = 0 + (c / ((a ** 2 + b ** 2 + c ** 2) ** 0.5)) * d
        
        return x, y, z
###################################################################################################
    @staticmethod
    def xyz_to_abc(x, y, z):
        d = math.sqrt(2) / 2
        a = y
        b = (x - a*d) / d
        c = -z
        # Calculate the a, b, and c values
        #a = x - 0
        #b = y - 0
        #c = z - 0
        return a, b, c