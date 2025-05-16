from vpython import *

scene.background = vector(0.1, 0.1, 0.1)  # Dark background
scene.title = "3D Cube model"
scene.width = 800
scene.height = 600

cube_center = vector(0, 0, 0)
thickness = 0.02
cubelet_length = 0.95

centre_position = {
    "white": vector(0, -1.5, 0), #bottom
    "yellow": vector(0, 1.5, 0), #top
    "red": vector(-1.5, 0, 0), #left
    "orange": vector(1.5, 0, 0), #right
    "blue": vector(0, 0, -1.5), #back
    "green": vector(0, 0, 1.5) #front
}

# Front face
for vec1 in [vector(0,0,0), vector(1, 0, 0), vector(-1, 0, 0), vector(0, 1, 0), vector(0, -1, 0), vector(1, 1, 0), vector(-1, -1, 0), vector(1, -1, 0), vector(-1, 1, 0)]:
    box(pos =cube_center + centre_position["green"] + vec1 , size=vector(cubelet_length, cubelet_length, thickness), color=color.green)

# Right face
for vec1 in [vector(0,0,0), vector(0, 0, 1), vector(0, 0, -1), vector(0, 1, 0), vector(0, -1, 0), vector(0,1,1), vector(0, -1, -1), vector(0, 1, -1), vector(0, -1, 1)]:
    box(pos =cube_center + centre_position["orange"] + vec1 , size=vector(thickness, cubelet_length, cubelet_length), color=color.orange)

# Back face
for vec1 in [vector(0,0,0), vector(1, 0, 0), vector(-1, 0, 0), vector(0, 1, 0), vector(0, -1, 0), vector(1, 1, 0), vector(-1, -1, 0), vector(1, -1, 0), vector(-1, 1, 0)]:
    box(pos =cube_center + centre_position["blue"] + vec1 , size=vector(cubelet_length, cubelet_length, thickness), color=color.blue)

# Left face
for vec1 in [vector(0,0,0), vector(0, 0, 1), vector(0, 0, -1), vector(0, 1, 0), vector(0, -1, 0), vector(0,1,1), vector(0, -1, -1), vector(0, 1, -1), vector(0, -1, 1)]:
    box(pos =cube_center + centre_position["red"] + vec1 , size=vector(thickness, cubelet_length, cubelet_length), color=color.red)

# Top face
for vec1 in [vector(0,0,0), vector(1, 0, 0), vector(-1, 0, 0), vector(0, 0, 1), vector(0, 0, -1), vector(1, 0, 1), vector(-1, 0, -1), vector(1, 0, -1), vector(-1, 0, 1)]:
    box(pos =cube_center + centre_position["yellow"] + vec1 , size=vector(cubelet_length, thickness, cubelet_length), color=color.yellow)

# Bottom face
for vec1 in [vector(0,0,0), vector(1, 0, 0), vector(-1, 0, 0), vector(0, 0, 1), vector(0, 0, -1), vector(1, 0, 1), vector(-1, 0, -1), vector(1, 0, -1), vector(-1, 0, 1)]:
    box(pos =cube_center + centre_position["white"] + vec1 , size=vector(cubelet_length, thickness, cubelet_length), color=color.white)

# Keep the window open
while True:
    pass  # Limit the loop to 100 iterations per second
