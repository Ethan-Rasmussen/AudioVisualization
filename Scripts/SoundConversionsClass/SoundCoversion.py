class SoundConversion:
    
    def __init__(self, a=None, b=None, c=None, x=None, y=None, z=None):
        if a is not None and b is not None and c is not None:
            self.a = a
            self.b = b
            self.c = c
            self.x, self.y, self.z = Conversion.abc_to_xyz(a, b, c)
        elif x is not None and y is not None and z is not None:
            self.x = x
            self.y = y
            self.z = z
            self.a, self.b, self.c = Conversion.xyz_to_abc(x, y, z)
        else:
            raise ValueError("Either (a, b, c) or (x, y, z) must be provided.")    
###################################################################################################
    @staticmethod
    def abc_to_xyz(a, b, c):
        # Define the arbitrary values
        x0, y0, z0 = 0, 0, 0
        d = 10
        
        # Solve for the x, y, z coordinates
        x = (a*d)/(d**2 + b**2 + c**2)**0.5
        y = (b*d)/(d**2 + a**2 + c**2)**0.5
        z = (c*d)/(d**2 + a**2 + b**2)**0.5
        
        # Translate the coordinates to the origin
        x -= x0
        y -= y0
        z -= z0
        
        return x, y, z
###################################################################################################
    @staticmethod
    def xyz_to_abc(x, y, z):
        d = math.sqrt(2) / 2
        a = y
        b = (x - a*d) / d
        c = -z
        return a, b, c