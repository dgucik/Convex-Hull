import numpy as np
import random
import math
#from PIL import Image, ImageDraw, ImageFont

POINTS_NUMBER = 5  # how many points
MAX_H_P = 300  # height of png file
MAX_W_P = 300  # height of png file
Y_OFFSET = 10  # multiplying x coords for png file
X_OFFSET = 10  # multiplying y coords for png file
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SHAPE_NAME = {
    "1": "POINT",
    "2": "LINE",
    "3": "TRIANGLE",
    "4": "QUADRANGLE",
    "5": "OTHER POLY"
}

# --------------------------------------------------------------------------------
class Point:
    global BLACK

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.angle = 0  # polar angle with P0
        self.color = BLACK

    def set_color(self, c: tuple) -> None:
        self.color = c


# --------------------------------------------------------------------------------------
# n - how many points to generate
class Generator:
    def __init__(self, n: int, v: list):
        # self.points = self.generate_fixed_points(v) # np.array(self.generate_points(n), dtype=object)
        self.points = np.array(self.generate_points(n), dtype=object)

    def generate_points(self, n: int) -> np.array:
        points = np.array([], dtype=object)
        p = set()
        while (len(p) < n):
            p.add((random.randint(3, 20), random.randint(3, 20)))

        for c in p:
            points = np.append(points, Point(c[0], c[1]))

        return points

    def generate_fixed_points(self, coords) -> np.array:
        return np.array([Point(x[0], x[1]) for x in coords], dtype=object)

    def get_points(self) -> np.ndarray:
        return self.points

    def print_points(self) -> None:
        for p in self.points:
            print(str(p.x) + " " + str(p.y))


class ComplexHull:
    def __init__(self, p: np.array):
        self.p = p  # list of points
        self.h = np.array([], dtype=object)  # list with solution

    def distance(self, p1: Point, p2: Point) -> float:
        return np.linalg.norm(np.array([p2.x, p2.y]) - np.array([p1.x, p1.y]))

    def angle(self, p1: Point, p2: Point) -> np.ndarray:
        return np.arctan2((p2.x - p1.x), (p2.y - p1.y))

    def check_shape(self, p: np.ndarray) -> int:
        if (p.size < 5):
            return SHAPE_NAME[str(p.size)]
        else:
            return SHAPE_NAME["5"]

    def check_if_line(self, p: np.ndarray) -> bool:
        res = []
        for x in range(2, p.size):
            res.append(self.check_orientation(p[x - 2], p[x - 1], p[x]))

        if ((len(set(res)) == 1) and (0 in set(res))):
            return True

        return False

    def check_orientation(self, p1: Point, p2: Point, p3: Point) -> int:

        o = (p3.y - p2.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p3.x - p2.x)

        if (o > 0):
            return -1  # clockwise
        elif (o < 0):
            return 1  # counterclockwise
        else:  # colilinear
            # print(f"Colinear!! ({p1.x} {p1.y}), ({p2.x} {p2.y}), ({p3.x} {p3.y})")
            if self.distance(p1, p2) < self.distance(p3, p1):
                return 0
            else:
                return 1
            # return 0

    def graham(self) -> np.array:
        # find the lowest y-coord and leftmost point, P0
        i_min = 0  # minimum index, will be needed for swapping
        y_min = self.p[0].y  # starting y coord of first point in array
        x_min = self.p[0].x  # starting x coord of first point in array

        for x in range(1, self.p.size):

            if (self.p[x].y < y_min) or ((y_min == self.p[x].y) and (self.p[x].x < x_min)):
                y_min = self.p[x].y
                x_min = self.p[x].x
                i_min = x

        p0 = self.p[i_min]  # save p0
        # print(f"p0: {p0.x}, {p0.y}")
        self.p = np.delete(self.p, i_min)  # delete p0 from array temp

        # sort depending on angle and distance
        self.p = np.array(sorted(self.p, key=lambda p: (self.angle(p0, p), self.distance(p0, p))), dtype=object)
        # self.p = np.array(sorted(self.p, key=lambda p: (self.angle(p0,p))), dtype=object)

        # add p0 at the beggining of the array
        self.p = np.insert(self.p, 0, p0)

        # scan begin
        self.h = self.p[0:2]

        for x in range(2, self.p.size):

            while (self.h.size >= 2) and (self.check_orientation(self.h[-2], self.h[-1], self.p[x]) != 1):
                self.h = self.h[:-1]

            self.h = np.append(self.h, self.p[x])

        # przypadek zdegenerowany
        while (self.h.size >= 2) and (self.check_orientation(self.h[-2], self.h[-1], self.h[0]) != 1):
            self.h = self.h[:-1]

        for h in self.h:
            h.color = RED
        # self.print_hull()

        #print(self.check_shape(self.h))
        return self.h

    # ------------- prints
    def print_results(self) -> None:
        pass

    def print_points(self) -> None:
        for p in self.p:
            print(str(p.x) + " " + str(p.y))

    def print_hull(self) -> None:
        for h in self.h:
            print(str(h.x) + " " + str(h.y) + " " + str(h.color))


# ------------------------------------------------------------------------
class Draw:
    global MAX_H_P, MAX_W_P, BLACK, WHITE, RED

    def __init__(self, points: np.array):
        self.points = points
        self.dot_size = 2
        self.image = Image.new("RGB", (MAX_H_P, MAX_W_P), WHITE)

    def draw_image(self) -> None:
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('tahoma.ttf', 7)
        draw.font = font

        # draw dots

        for p in self.points:
            y1 = MAX_H_P - (p.y * Y_OFFSET)
            draw.ellipse((p.x * X_OFFSET - 1, y1 - 1, p.x * X_OFFSET + 1, y1 + 1), outline=p.color)
            draw.text((p.x * X_OFFSET, MAX_H_P - ((p.y * Y_OFFSET) - 5)), f"( {p.x},  {p.y} )", fill=(0, 0, 0))
        self.image.save(f"points{random.randint(100, 456)}.png")

