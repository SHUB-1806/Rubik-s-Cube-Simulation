from vpython import *
from numpy import pi

# Create a scene
scene = canvas(title='Rotating Cube', width=800, height=600, background=color.white)

#creating a box at origin
cube = box(pos=vector(0, 0, 0), size=vector(1, 1, 1), color=color.red)

#function to convert degree to radian
def radian(degree):
    return degree * (pi / 180)

while True:
    rate(60)
    cube.rotate(angle= radian(1), axis=vector(0, 1, 0))