from vpython import *

spacing = 1.1  

for x in [-1, 0, 1]:
    for y in [-1, 0, 1]:
        for z in [-1, 0, 1]:
            box(pos=vector(x*spacing, y*spacing, z*spacing), size=vector(1,1,1), color=color.white)

while True:
    pass
# The above code creates a 3D grid of cubes in VPython, representing the cubelets of a Rubik's Cube.
