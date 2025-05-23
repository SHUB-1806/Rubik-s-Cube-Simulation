

from vpython import *

scene = canvas(title='Vertical Tower of Cubes', width=800, height=600, background=color.white)

colours = [color.red, color.green, color.blue, color.yellow, color.orange]
color_names = ["Red", "Green", "Blue", "Yellow", "Orange"]

list_of_box = [None]*5

for i in range(5):
    y = i - 2
    list_of_box[i] = box(pos=vector(0, y, 0), size=vector(1, 1, 1), color=colours[i])
    label(
        pos=vector(0, y , 0),  # Slightly above the top of the cube
        text=color_names[i],
        height=15,
        color=color.black
    )

while True:
    rate(30)
