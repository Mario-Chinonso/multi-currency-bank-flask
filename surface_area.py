import numpy as np
import math as mt




# Finding the Total Surface Area of a Cube (a = length of side of the cube)
def surface_area_of_a_cube(a):
    return 6 * a ** 2


# Finding the length of side of a cube from the Total surface Area
def length_of_a_cube(A):
     return mt.sqrt(A / 6)


def surface_area_of_a_cuboid(l, b, h):
     return 2 * (l* b + l * h + b * h)

lenth = np.array([[9], 
                [11], 
                [11.3], 
                [130], 
                [11.2], 
                [3.5], 
                [4], 
                [7.5], 
                [34.5], 
                [0.29]])

breadth = np.array([[4], 
                    [7], 
                    [6.7], 
                    [97], 
                    [4.75], 
                    [2], 
                    [3], 
                    [3.4], 
                    [52.5], 
                    [0.16]])

height = np.array([[7], 
                  [13], 
                  [5.3], 
                  [65], 
                  [2.5], 
                  [3], 
                  [6], 
                  [6.8], 
                  [2.75], 
                  [0.23]])

x = surface_area_of_a_cuboid(lenth[9], breadth[9], height[9])
print(x)





lengths = np.array([[6], [11], [7.5], [19.7], [0.7]])

areas = np.array([surface_area_of_a_cube(lengths)])
print(areas)
print()


print("The surface area of a cube with the side 6cm is: ",surface_area_of_a_cube(6))
print("The surface area of a cube with the side 11cm is: ",surface_area_of_a_cube(11))
print("The surface area of a cube with the side 7.5cm is: ",surface_area_of_a_cube(7.5))
print("The surface area of a cube with the side 19.7cm is: ",surface_area_of_a_cube(19.7))
print("The surface area of a cube with the side 0.7cm is: ",surface_area_of_a_cube(0.7))

print()
print("The length of a cube with Total Surface Area of 181.5cm^2 is: ", length_of_a_cube(181.5))
print("The length of a cube with Total Surface Area of 294cm^2 is: ", length_of_a_cube(294))
print("The length of a cube with Total Surface Area of 13.5cm^2 is: ", length_of_a_cube(13.5))
print("The length of a cube with Total Surface Area of 0.375cm^2 is: ", length_of_a_cube(0.375))
print("The length of a cube with Total Surface Area of 864cm^2 is: ", length_of_a_cube(864))