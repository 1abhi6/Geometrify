import math

class Coordinate():
    """
    A class representing a point in two-dimensional space.

    Attributes:
        x (float or int): The x-coordinate of the point.
        y (float or int): The y-coordinate of the point.
    """
    def __init__(self, x, y):
        """
        Initializes a new instance of the Coordinate class.

        Args:
            x (float or int): The x-coordinate of the point.
            y (float or int): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a string representation of the Coordinate object.

        Returns:
            A string in the format "(x,y)".
        """
        return f"({self.x},{self.y})"

    # Basic operations such as addition, substraction, multiplication and division of the coordinates
    def __add__(self, other):
        """
        Adds the coordinates of two Coordinate objects and returns a new Coordinate object.

        Args:
            other (Coordinate): The other Coordinate object to add.

        Returns:
            A new Coordinate object representing the sum of the two coordinates.
        """
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Overloads the '-' operator to calculate the difference between two coordinates.

        Args:
            other: The other Coordinate object to subtract from this one.

        Returns:
            A new Coordinate object representing the difference between the two coordinates.
        """
        return Coordinate(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """
        Overloads the '*' operator to calculate the element-wise product between two coordinates.

        Args:
            other: The other Coordinate object to multiply with this one.

        Returns:
            A new Coordinate object representing the element-wise product between the two coordinates.
        """
        return Coordinate(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        """
        Overloads the '/' operator to calculate the element-wise division between two coordinates.

        Args:
            other: The other Coordinate object to divide this one by.

        Returns:
            A new Coordinate object representing the element-wise division between the two coordinates.
        """
        return Coordinate(self.x / other.x, self.y / other.y)

    # Distance calculation
    def distance(self, other):
        """
        Calculates the Euclidean distance between two coordinates.

        Args:
            other: The other Coordinate object to calculate the distance to.

        Returns:
            The distance between the two coordinates as a float.
        """
        return round(((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5, 3)

    # Midpoint calculation
    def midpoint(self, other):
        """
        Calculates the midpoint between this coordinate and another.

        Args:
            other (Coordinate): The other Coordinate object to calculate the midpoint with.

        Returns:
            A new Coordinate object representing the midpoint between this coordinate and the other.
        """
        return Coordinate((self.x + other.x) / 2, (self.y + other.y) / 2)

    # Slope calculation
    def slope(self, other):
        """
        Calculates the slope between this coordinate and another.

        Args:
            other (Coordinate): The other Coordinate object to calculate the slope with.

        Returns:
            The slope between this coordinate and the other as a float. If the x-coordinates are equal, returns infinity.
        """
        if self.x == other.x:
            # The x coordinates are the same, so the slope is undefined
            return math.inf
        else:
            return round((other.y - self.y) / (other.x - self.x), 3)

    # Angle calculation with respect to positive X axis

    def angle_with_positive_X(self, other):
        """
        Calculates the angle of line with respect to positive X axis

        Args:
            other (Coordinate): The other Coordinate object to calculate the angle with.

        Returns:
            The angle of line with respect to positive X axis in degrees as a float.
        """
        dx = other.x - self.x
        dy = other.y - self.y
        radians = math.atan2(dy, dx)
        degrees = round(math.degrees(radians), 3)
        return degrees

    # Angle calculation with respect to positive Y axis
    def angle_with_positive_Y(self, other):
        """
        Calculates the angle of line with respect to positive Y axis

        Args:
            other (Coordinate): The other Coordinate object to calculate the angle with.

        Returns:
            The angle of line with respect to positive Y axis in degrees as a float.
        """
        angle = self.angle_with_positive_X(other)
        return (90-angle)

    # Angle between two lines given their slopes
    @staticmethod
    def angle_between_slopes(m1, m2):
        """
        Calculates the angle between two lines given their slopes.

        Args:
            m1 (float): The slope of the first line.
            m2 (float): The slope of the second line.

        Returns:
            The angle between the two lines in degrees as float.
        """
        angle = abs((m2 - m1) / (1 + m1 * m2))

        # Calculate tan inverse of the angle
        ret = math.atan(angle)

        # Convert the angle from radian to degree
        val = (ret * 180) / math.pi
        return round(val, 3)

    # Calculates the area of a triangle formed by three coordinates
    def triangle_area(self, other1, other2):
        """
        Calculates the area of a triangle formed by three coordinates.

        Args:
            other1 (Coordinate): The first coordinate of the triangle.
            other2 (Coordinate): The second coordinate of the triangle.

        Returns:
            The area of the triangle formed by the three coordinates.
        """
        return abs((self.x * (other1.y - other2.y) + other1.x * (other2.y - self.y) + other2.x * (self.y - other1.y)) / 2)

    # Reflect a point about a line

    def reflect(self, line_start, line_end):
        """
        Reflects a given Coordinate object about a line formed by two other Coordinate objects.

        Args:
            line_start (Coordinate): The start point of the line.
            line_end (Coordinate): The end point of the line.

        Returns:
            Coordinate: A new Coordinate object representing the reflected point.
        """
        # Calculate the slope and y-intercept of the line
        slope = line_start.slope(line_end)
        intercept = line_start.y - slope * line_start.x

        # Calculate the slope and y-intercept of the perpendicular bisector passing through the given point
        perpendicular_slope = -1 / slope
        perpendicular_intercept = self.y - perpendicular_slope * self.x
        intersection_x = (perpendicular_intercept - intercept) / \
            (slope - perpendicular_slope)
        intersection_y = slope * intersection_x + intercept
        reflected_x = round(2 * intersection_x - self.x, 3)
        reflected_y = round(2 * intersection_y - self.y, 3)
        return Coordinate(reflected_x, reflected_y)

    # Translate a point
    def translate(self, dx, dy):
        """
        Translates the Coordinate object by a given amount.

        Args:
            dx (float or int): The amount to translate in the x direction.
            dy (float or int): The amount to translate in the y direction.

        Returns:
            Coordinate: A new Coordinate object representing the translated point.
        """
        return Coordinate(self.x + dx, self.y + dy)

    # Scale a point
    def scale(self, factor):
        """
        Scale the current point by a given factor.

        Args:
            factor (float or int): The scaling factor.

        Returns:
            Coordinate: A new instance of the Coordinate class representing the scaled point.
        """
        return Coordinate(self.x * factor, self.y * factor)

    # Find the intersection point of two lines
    @staticmethod
    def line_intersection(other1_start, other1_end, other2_start, other2_end):
        """
        Computes the intersection point of two lines defined by four points.

        Args:
            other1_start (Coordinate): The starting point of the first line.
            other1_end (Coordinate): The ending point of the first line.
            other2_start (Coordinate): The starting point of the second line.
            other2_end (Coordinate): The ending point of the second line.

        Returns:
            Coordinate: The intersection point of the two lines.
        """
        slope1 = other1_start.slope(other1_end)
        intercept1 = other1_start.y - slope1 * other1_start.x
        slope2 = other2_start.slope(other2_end)
        intercept2 = other2_start.y - slope2 * other2_start.x
        intersection_x = round(
            (intercept2 - intercept1) / (slope1 - slope2), 3)
        intersection_y = round(slope1 * intersection_x + intercept1, 3)
        return Coordinate(intersection_x, intersection_y)

    # Find the distance between a point and a line
    def distance_to_line(self, line_start, line_end):
        """
        Computes the perpendicular distance from the current point to the line
        defined by two other points.

        Args:
            line_start (Coordinate): The starting point of the line.
            line_end (Coordinate): The ending point of the line.

        Returns:
            float: The distance from the current point to the line.
        """
        numerator = abs((line_end.y - line_start.y) * self.x - (line_end.x - line_start.x)
                        * self.y + line_end.x * line_start.y - line_end.y * line_start.x)
        denominator = ((line_end.y - line_start.y) ** 2 +
                       (line_end.x - line_start.x) ** 2) ** 0.5
        return round((numerator / denominator), 3)

    # Find the equation of a line
    def line_equation(self, point2):
        """
        Computes the equation of the line passing through two points.

        Args:
            point2 (Coordinate): The second point on the line.

        Returns:
            str: A string representation of the equation of the line.
        """
        slope = round(self.slope(point2), 3)
        intercept = round(self.y - slope * self.x, 3)
        return f"y = {slope}x + ({intercept})"

    # Find the area of quadrilateral created by four points
    def quadrilateral_area(self, point2, point3, point4):
        """
        Calculates the area of a quadrilateral created by four points.

        Args:
            point2: The second point of the quadrilateral.
            point3: The third point of the quadrilateral.
            point4: The fourth point of the quadrilateral.

        Returns:
            The area of the quadrilateral as a float.
        """
        side1 = self.distance(point2)
        side2 = point2.distance(point3)
        side3 = point3.distance(point4)
        side4 = point4.distance(self)
        side = (side1 + side2 + side3 + side4) / 2
        return round(math.sqrt((side - side1) * (side - side2) * (side - side3) * (side - side4)), 3)

    # Find the perimeter of quadrilateral created by four points

    def quadrilateral_perimeter(self, point2, point3, point4):
        """
        Calculates the perimeter of a quadrilateral created by four points.

        Args:
            point2: The second point of the quadrilateral.
            point3: The third point of the quadrilateral.
            point4: The fourth point of the quadrilateral.

        Returns:
            The perimeter of the quadrilateral as a float.
        """
        return round(self.distance(point2) + point2.distance(point3) + point3.distance(point4) + point4.distance(self), 3)