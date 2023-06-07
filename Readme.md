![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/pypi/v/Geometrify)
![Format](https://img.shields.io/pypi/format/Geometrify)
# Geometrify

Geometrify is a Python package for working with 2D coordinate geometry. It provides a comprehensive set of tools for performing operations such as distance calculation, angle measurement, rotation, translation, and scaling of geometries. With Geometrify, you can easily create, manipulate, and analyze complex 2D geometries with ease.

## Usage

- Make sure you have installed Python in your system.
- Run the following command in Command Prompt.

```
pip install Geometrify
```

## Example

```
from Geometrify import Coordinate

# Create two coordinate points
point1 = Coordinate(1, 2)
point2 = Coordinate(4, 5)
```

### Basic Operations

```
# Basic operations such as addition, subtraction, multiplication and division of the coordinates
added_point = point1 + point2 # Coordinate(5, 7)
substracted_point = point1 - point2 # Coordinate(-3, -3)
multiplied_point = point1 * point2 # Coordinate(4, 10)
divided_point = point1 / point2 # Coordinate(0.25, 0.4)
```

### Distance calculation

```
distance = point1.distance(point2) # 4.243
```

### Midpoint calculation

```
midpoint = point1.midpoint(point2) # Coordinate(2.5, 3.5)
```

### Slope calculation

```
slope = point1.slope(point2) # 1.0
```

### Angle calculation with respect to positive X-axis

```
point2.angle_with_positive_x(point3) # 18.435
```

### Angle calculation with respect to positive Y-axis

```
point2.angle_with_positive_y(point3) # 71.565
```

### Angle between two lines given their slopes

```
angle = Coordinate.angle_between_slopes(1.75,0.27) # 45.146
```

### Calculates the area of a triangle formed by three coordinates

```
point3 = Coordinate(7, 6)
triangle_area = point1.triangle_area(point2, point3) # 3.0
```

### Reflect a point about a line

```
line_start = Coordinate(0, 0)
line_end = Coordinate(1, 1)
reflected_point = point1.reflect(line_start, line_end) # Coordinate(2.0, 1.0)
```

### Translate a point

```
translated_point = point1.translate(2, 3) # Coordinate(3, 5)
```

### Scale a point

```
scaled_point = point1.scale(2) # Coordinate(2, 4)
```

### Intersection point of two lines

```
point4 = Coordinate(23,12)
intersection = Coordinate.line_intersection(point1,point2,point3,point4) # Coordinate(3.8,4.8)
```

### Distance between a point and a line

```
# Create two Coordinate objects to represent the start and end points of a line
line_start = Coordinate(1, 1)
line_end = Coordinate(4, 5)

# Create a third Coordinate object to represent a point
point = Coordinate(2, 3)

# Use the distance_to_line method to calculate the distance between the point and the line
distance = point.distance_to_line(line_start, line_end) # 0.4
```

### Equation of the line passing through two points

```
equation = line_start.line_equation(line_end) # y = 1.333x + (-0.333)
```

