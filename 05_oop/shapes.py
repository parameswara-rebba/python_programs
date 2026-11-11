"""Inheritance and polymorphism with an abstract Shape class."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return (
            f"{type(self).__name__}: area={self.area():.2f}, "
            f"perimeter={self.perimeter():.2f}"
        )


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)


if __name__ == "__main__":
    for shape in (Circle(1), Rectangle(3, 4), Square(2)):
        print(shape.describe())
