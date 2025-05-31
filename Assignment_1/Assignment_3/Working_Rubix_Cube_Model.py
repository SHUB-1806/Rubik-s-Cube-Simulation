from vpython import *

#setting up the canvas
scene.background = vector(0.1, 0.1, 0.1)
scene.width = 800
scene.height = 600
scene.title = "Working 3D Cube model"
scene.forward = vector(-1, -1, -1)  # Camera looks along negative z-axis from a distance


# Defining the cube center, thickness, and cubelet length
cube_center = vector(0, 0, 0)
thickness = 0.02
cubelet_length = 0.95

# Defining the center position for each face of the cube
centre_position = {
    "D": vector(0, -1.5, 0),  # bottom
    "U": vector(0, 1.5, 0),  # top
    "L": vector(-1.5, 0, 0),    # left
    "R": vector(1.5, 0, 0),  # right
    "B": vector(0, 0, -1.5),   # back
    "F": vector(0, 0, 1.5)    # front
}

# Defining the face directions for rotation
axis_vectors = {
    "U": vector(0, 1, 0),
    "D": vector(0, -1, 0),
    "F": vector(0, 0, 1),
    "B": vector(0, 0, -1),
    "L": vector(-1, 0, 0),
    "R": vector(1, 0, 0)
}

# Defining the face directions
vec_F = [vector(i, j, 0) for j in range(1, -2, -1) for i in range(-1, 2)]
vec_U = [vector(i, 0, k) for k in range(-1,2) for i in range(-1, 2)]
vec_R = [vector(0, j, k) for j in range(1, -2, -1) for k in range(1, -2, -1)]
vec_L = [vector(0, j, k) for j in range(1, -2, -1) for k in range(-1, 2)]
vec_B = [vector(i, j, 0) for j in range(1, -2, -1) for i in range(1, -2, -1)]
vec_D = [vector(i, 0, k) for k in range(1, -2, -1) for i in range(-1, 2)]

#__________this is simply this___________
# vec1 in [vector(-1,1,0), vector(0,1,0), vector(1,1,0), vector(-1,0,0), vector(0,0,0), vector(1,0,0), vector(-1,-1,0), vector(0,-1,0), vector(1,-1,0)]:

#front face

# cubelets_by_face = {
#     "F": {f"F{i}": None for i in range(1, 10)},
#     "R": {f"R{i}": None for i in range(1, 10)},
#     "B": {f"B{i}": None for i in range(1, 10)},
#     "L": {f"L{i}": None for i in range(1, 10)},
#     "U": {f"U{i}": None for i in range(1, 10)},
#     "D": {f"D{i}": None for i in range(1, 10)}
# }
cubelets_by_face = {face: {} for face in ["F", "U", "L", "B", "D", "R"]}

# Initializing the cubelets for each face and putting them in the dictionary
for idx in range(9):
    key = "F" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["F"] + vec_F[idx],
                  size = vector(cubelet_length, cubelet_length, thickness),
                  color = color.green)
    cubelets_by_face["F"][key] = cubelet

    key = "U" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["U"] + vec_U[idx],
                  size = vector(cubelet_length, thickness, cubelet_length),
                  color = color.yellow)
    cubelets_by_face["U"][key] = cubelet

    key = "L" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["L"] + vec_L[idx],
                  size = vector(thickness, cubelet_length, cubelet_length),
                  color = color.red)
    cubelets_by_face["L"][key] = cubelet

    key = "B" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["B"] + vec_B[idx],
                  size = vector(cubelet_length, cubelet_length, thickness),
                  color = color.blue)
    cubelets_by_face["B"][key] = cubelet

    key = "D" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["D"] + vec_D[idx],
                  size = vector(cubelet_length, thickness, cubelet_length),
                  color = color.white)
    cubelets_by_face["D"][key] = cubelet

    key = "R" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["R"] + vec_R[idx],
                  size = vector(thickness, cubelet_length, cubelet_length),
                  color = color.orange)
    cubelets_by_face["R"][key] = cubelet

# grouping cubelets by face for rotation
group_for_rotation = {

    "F":
        [cubelets_by_face["F"][f"F{i}"] for i in range(1, 10)] +
        [cubelets_by_face["U"][f"U{i}"] for i in range(7, 10)] +
        [cubelets_by_face["D"][f"D{i}"] for i in range(1, 4)] +
        [cubelets_by_face["R"][f"R{i}"] for i in range(1, 10, 3)] +
        [cubelets_by_face["L"][f"L{i}"] for i in range(3, 10, 3)]
    ,

    "B" : 
        [cubelets_by_face["B"][f"B{i}"] for i in range(1, 10)]+
        [cubelets_by_face["U"][f"U{i}"] for i in range(1, 4)]+
        [cubelets_by_face["D"][f"D{i}"] for i in range(7, 10)]+
        [cubelets_by_face["R"][f"R{i}"] for i in range(3, 10, 3)]+
        [cubelets_by_face["L"][f"L{i}"] for i in range(1, 10, 3)]
    ,

    "U" : 
        [cubelets_by_face["U"][f"U{i}"] for i in range(1, 10)]+
        [cubelets_by_face["F"][f"F{i}"] for i in range(1, 4)]+
        [cubelets_by_face["B"][f"B{i}"] for i in range(1, 4)]+
        [cubelets_by_face["R"][f"R{i}"] for i in range(1, 4)]+
        [cubelets_by_face["L"][f"L{i}"] for i in range(1, 4)]
    ,
    "D" : 
        [cubelets_by_face["D"][f"D{i}"] for i in range(1, 10)]+
        [cubelets_by_face["F"][f"F{i}"] for i in range(7, 10)]+
        [cubelets_by_face["B"][f"B{i}"] for i in range(7, 10)]+
        [cubelets_by_face["R"][f"R{i}"] for i in range(7, 10)]+
        [cubelets_by_face["L"][f"L{i}"] for i in range(7, 10)]
    ,
    "L" : 
        [cubelets_by_face["L"][f"L{i}"] for i in range(1, 10)]+
        [cubelets_by_face["U"][f"U{i}"] for i in range(1, 10, 3)]+
        [cubelets_by_face["D"][f"D{i}"] for i in range(1, 10, 3)]+
        [cubelets_by_face["F"][f"F{i}"] for i in range(1, 10, 3)]+
        [cubelets_by_face["B"][f"B{i}"] for i in range(3, 10, 3)]
    ,
    "R" : 
        [cubelets_by_face["R"][f"R{i}"] for i in range(1, 10)]+
        [cubelets_by_face["U"][f"U{i}"] for i in range(3, 10, 3)]+
        [cubelets_by_face["D"][f"D{i}"] for i in range(3, 10, 3)]+
        [cubelets_by_face["F"][f"F{i}"] for i in range(3, 10, 3)]+
        [cubelets_by_face["B"][f"B{i}"] for i in range(1, 10, 3)]
    
}
# Function to clockwise rotate a face of the cube
def rotate_face(face):
    global rotation_axis, rotation_center, face_cubes

    face_cubes = group_for_rotation[face]
    rotation_axis = axis_vectors[face]
    rotation_center = cube_center

    total_angle = radians(90)
    steps = 10
    dtheta = total_angle / steps

    for _ in range(steps):
        rate(60)  # Controls animation speed
        for item in face_cubes:
            item.rotate(angle=dtheta, axis=rotation_axis, origin=rotation_center)

# def rotate_face(face):
#     global rotation_axis, rotation_center, face_cubes
    
    
#     face_cubes = group_for_rotation[face]
    
#     # Set rotation parameters based on face
#     rotation_axis = axis_vectors[face]
#     rotation_center = cube_center


#     # Rotate the cubes
#     for item in face_cubes:
#         item.rotate(angle=radians(90), axis=rotation_axis, origin=rotation_center)


def key_pressed(evt):  # info about event is stored in evt
    keyname = evt.key.upper()  # Convert key to uppercase for consistency

    #changing according to notations given in assignmemnt
    if keyname == 'J': #J is for Top Faace clockwise rotation
        keyname = 'U'
    elif keyname == 'S': #S is for Bottom Face clockwise rotation
        keyname = 'D' # note this D is not ACW bottom face rotation its clockwise bottom face rotation
    elif keyname == 'H': #H is for Front Face clockwise rotation
        keyname = 'F'
    elif keyname == 'W': #W is for Back Face clockwise rotation
        keyname = 'B'
    elif keyname == 'D': #D is for Left Face clockwise rotation
        keyname = 'L'
    elif keyname == 'K': #K is for Right Face clockwise rotation
        keyname = 'R'

    if keyname in axis_vectors:
        rotate_face(keyname)
    else:
        print(f"{keyname} is not a valid key for rotation.")

scene.bind('keydown', key_pressed)

# Keep the window open
while True:
    rate(60)  # Limit the loop to 60 iterations per second
    # This keeps the window responsive and allows for key events to be processed