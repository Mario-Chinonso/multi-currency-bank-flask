import numpy as np
import math as mt


def surface_area_of_a_cube(a):
    return 6 * a ** 2


def volume_of_a_cube(a):
    return a ** 3


def volume_of_a_cuboid(l, b, h):
    return l * b * h

def surface_area_of_a_cuboid(l, b, h):
    return 2 * ((l * b) + (b * h) + (l * h))

def volume_of_a_cylinder(r, h):
    return mt.pi * r ** 2 * h

def curved_surface_area_of_a_cylinder(r, h):
    return 2 * mt.pi * r *h

def total_surface_area_of_a_cylinder(r, h):
    return 2 * mt.pi * r * (h + r)

def volume_of_a_cone(r, h):
    return 0.3333333333333333 * mt.pi * r ** 2 * h

def curved_surface_area_of_a_cone(r, l):
    return mt.pi * r * l


def total_surface_area_of_a_cone(r, l):
    return mt.pi * r * (l + r)

def areas_of_solid_shapes():
    while True:
        print("\nHey😏. So let's begin some area and volume calculations.你好，我来打算一点数学。")
        print("1. Volume.")
        print("2. Surface Area.")
        print("3. Curved Surface Area.")
        print("4. Total Surface Area.")

if __name__ == "__main__":
    areas_of_solid_shapes()
        









