from __future__ import annotations
from enum import Enum
import math
import random


class Themes(Enum):
    White = 0
    Black = 1
    Light = 2
    Dark = 3
    CyberSpace = 4
    TurquoiseHexagon = 5


class Color:
    pass

    def get_hex(self):
        pass

    def get_rgba(self):
        pass


class ColorRGBA(Color):

    def __init__(self, r: int, g: int, b: int, a: int = 255):
        self.r = max(0, min(r, 255))
        self.g = max(0, min(g, 255))
        self.b = max(0, min(b, 255))
        self.a = max(0, min(a, 255))

    def get_hex(self):
        if self.a is not None:
            return "#{:02x}{:02x}{:02x}{:02x}".format(self.r, self.g, self.b, self.a).upper()
        else:
            return "#{:02x}{:02x}{:02x}".format(self.r, self.g, self.b)

    def get_rgba(self):
        return self.r, self.g, self.b, self.a


class ColorHEX(Color):

    def __init__(self, color):
        if color[0] != '#':
            color = '#' + color
        self.color = color

    def __str__(self):
        return self.color

    def get_hex(self):
        return self.color

    def get_rgba(self):
        hex_code = self.color.lstrip('#')
        r, g, b, a = tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4, 6))
        return r / 255.0, g / 255.0, b / 255.0, a / 255.0


def generate_random_array(
        amount: int = 10,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0
) -> list[float]:
    """Generate a list of random numbers.

    Args:
        amount: The length of the list.
        min_value: Minimum possible value of any given number.
        max_value: Maximum possible value of any given number.
    """
    data = []
    for i in range(amount):
        data.append(round(random.uniform(min_value, max_value), 3))
    return data


def generate_progressive_array(
        amount: int = 10,
        starting_from: int = 0
) -> list[int]:
    """Generate a list of progressive integers.

    Args:
        amount: The length of the list.
        starting_from: The value of the first list element.
    """
    data = []
    for i in range(starting_from, starting_from + amount):
        data.append(i)
    return data


def generate_Box3D_data(
        amount: int = 25,
        starting_from: int = 0,
        min_height: int | float = 0.0,
        max_height: int | float = 10.0
):
    """Generate random data for Box3D chart.

    Args:
        amount: The length of the data.
        starting_from: The first x value.
        min_height: Minimum possible height for any given box.
        max_height: Maximum possible height for any given box.

    Returns:
        List of Box3D entries.
    """
    data = []
    root = int(math.sqrt(amount))
    for x in range(starting_from, root):
        for z in range(starting_from, root):
            height = random.uniform(min_height, max_height)
            data.append({
                'xCenter': x,
                'yCenter': min_height + height / 2,
                'zCenter': z,
                'xSize': 1,
                'ySize': height,
                'zSize': 1
            })
    return data


def generate_random_xy_data(
        amount: int = 1,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0
) -> list[dict[str, int | float]]:
    """Generate n amount of random XY datapoints in a specific value range.

    Args:
        amount (int): The size of the generated dataset.
        min_value (int | float): Minimum value of any given datapoint.
        max_value (int | float): Maximum value of any given datapoint.

    Returns:
        List of dictionaries containing x and y values.
    """
    data = []
    for i in range(amount):
        data.append({
            'x': round(random.uniform(min_value, max_value), 3),
            'y': round(random.uniform(min_value, max_value), 3),
        })
    return data


def generate_random_xyz_data(
        amount: int = 1,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0
) -> list[dict[str, int | float]]:
    """Generate n amount of random XYZ datapoints in a specific value range.

        Args:
            amount (int): The size of the generated dataset.
            min_value (int | float): Minimum value of any given datapoint.
            max_value (int | float): Maximum value of any given datapoint.

        Returns:
            List of dictionaries containing x, y, and z values.
    """
    data = []
    for i in range(amount):
        data.append({
            'x': round(random.uniform(min_value, max_value), 3),
            'y': round(random.uniform(min_value, max_value), 3),
            'z': round(random.uniform(min_value, max_value), 3),
        })
    return data


def generate_progressive_xy_data(
        amount: int = 100,
        starting_from: int = 0,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0,
        progressive_axis: str = 'x'
) -> list[dict[str, int | float]]:
    """Generate n amount of XY datapoints that are progressive with respect to one axis.

    Args:
        amount (int): The size of the generated dataset.
        starting_from (int): The starting point of the progressive axis.
        min_value (int | float): Minimum value of any given datapoint.
        max_value (int | float): Maximum value of any given datapoint.
        progressive_axis (str): "x" or "y"

    Returns:
        List of dictionaries containing x and y values.
    """
    data = []
    if progressive_axis == 'x':
        for i in range(starting_from, starting_from + amount):
            data.append({
                'x': i,
                'y': round(random.uniform(min_value, max_value), 3),
            })
    elif progressive_axis == 'y':
        for i in range(starting_from, starting_from + amount):
            data.append({
                'x': round(random.uniform(min_value, max_value), 3),
                'y': i,
            })
    return data


def generate_progressive_xyz_data(
        amount: int = 100,
        starting_from: int = 0,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0,
        progressive_axis: str = 'x'
) -> list[dict[str, int | float]]:
    """Generate n amount of XYZ datapoints that are progressive with respect to one axis.

    Args:
        amount (int): The size of the generated dataset.
        starting_from (int): The starting point of the progressive axis.
        min_value (int | float): Minimum value of any given datapoint.
        max_value (int | float): Maximum value of any given datapoint.
        progressive_axis (str): "x", "y", or "z"

    Returns:
        List of dictionaries containing x, y, and z values.
    """
    data = []
    if progressive_axis == 'x':
        for i in range(starting_from, starting_from + amount):
            data.append({
                'x': i,
                'y': round(random.uniform(min_value, max_value), 3),
                'z': round(random.uniform(min_value, max_value), 3),
            })
    elif progressive_axis == 'y':
        for i in range(starting_from, starting_from + amount):
            data.append({
                'x': round(random.uniform(min_value, max_value), 3),
                'y': i,
                'z': round(random.uniform(min_value, max_value), 3),
            })
    elif progressive_axis == 'z':
        for i in range(starting_from, starting_from + amount):
            data.append({
                'x': round(random.uniform(min_value, max_value), 3),
                'y': round(random.uniform(min_value, max_value), 3),
                'z': i,
            })
    return data


def generate_random_matrix_data(
        columns: int,
        rows: int,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0
) -> list[list[int | float]]:
    """Generate a (2D) matrix dataset with random values between a specific range.

    Args:
        columns (int): The amount of columns in the matrix.
        rows (int): The amount of rows in the matrix.
        min_value (int | float): Minimum value of any given point in the matrix.
        max_value (int | float): Maximum value of any given point in the matrix.

    Returns:
        List of lists containing values.
    """
    data = [
        [round(random.uniform(min_value, max_value), 3) for j in range(columns)]
        for i in range(rows)
    ]
    return data
