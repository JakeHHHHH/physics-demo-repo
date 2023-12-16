
import math

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y}, {self.z})'
    
    def __str__(self) -> str:
        return f"{self.x}i + {self.y}j + {self.z}k"
    
    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        if item == 2:
            return self.z
        else:
            raise IndexError 
        
    def __add__(self, other):
        return Vector(
        self.x + other.x,
        self.y + other.y,
        self.z + other.z,
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z,
            )
        elif isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other,
            )
        else:
            raise TypeError
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
    def __cross__(self, other):
        return Vector(
            self.y * other.z - other.y * self.z,
            -1 * (self.x * other.z - self.z * other.x),
            self.x * other.y - self.y - other.x
        )
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z **2)
    
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )