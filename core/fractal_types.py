from enum import Enum

class FractalCategory:
    COMPLEX = "Complex"
    GEOMETRIC = "Geometric"
    SYSTEM = "System"

class FractalType(Enum):
    # Комплексные фракталы
    MANDELBROT = (1, FractalCategory.COMPLEX)
    JULIA = (2, FractalCategory.COMPLEX)
    BURNING_SHIP = (3, FractalCategory.COMPLEX)
    NEWTON = (4, FractalCategory.COMPLEX)
    TRICORN = (5, FractalCategory.COMPLEX)
    
    # Геометрические фракталы
    PYTHAGORAS_TREE = (6, FractalCategory.GEOMETRIC)
    LEVY_CURVE = (7, FractalCategory.GEOMETRIC)
    SIERPINSKI = (8, FractalCategory.GEOMETRIC)
    DRAGON_CURVE = (9, FractalCategory.GEOMETRIC)  
    SIERPINSKI_CARPET = (10, FractalCategory.GEOMETRIC)  
    
    # Системные фракталы
    KOCH_SNOWFLAKE = (11, FractalCategory.SYSTEM)
    
    def __new__(cls, value, category):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.category = category
        return obj
    
    @property
    def max_depth(self):
        limits = {
            FractalType.PYTHAGORAS_TREE: 12,
            FractalType.LEVY_CURVE: 15,
            FractalType.SIERPINSKI: 10,
            FractalType.KOCH_SNOWFLAKE: 7,
            FractalType.SIERPINSKI_CARPET: 5
        }
        return limits.get(self, 15)