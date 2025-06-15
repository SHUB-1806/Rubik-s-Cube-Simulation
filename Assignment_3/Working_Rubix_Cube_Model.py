from vpython import *



def update_stickers_after_U(cubelets_by_face):
    cu, cf, cl, cb, cr = [cubelets_by_face[f] for f in "UFLBR"]

    cu["U1"], cu["U2"], cu["U3"], cu["U4"], cu["U5"], cu["U6"], cu["U7"], cu["U8"], cu["U9"] = \
        cu["U7"], cu["U4"], cu["U1"], cu["U8"], cu["U5"], cu["U2"], cu["U9"], cu["U6"], cu["U3"] 
    
    temp_f = [cf[f"F{i}"] for i in range(1, 4)]
    temp_l = [cl[f"L{i}"] for i in range(1, 4)]
    temp_b = [cb[f"B{i}"] for i in range(1, 4)]
    temp_r = [cr[f"R{i}"] for i in range(1, 4)]

    cf["F1"], cf["F2"], cf["F3"] = temp_r
    cl["L1"], cl["L2"], cl["L3"] = temp_f
    cb["B1"], cb["B2"], cb["B3"] = temp_l
    cr["R1"], cr["R2"], cr["R3"] = temp_b

def update_stickers_after_D(cubelets_by_face):
    cd, cf, cl, cb, cr = [cubelets_by_face[f] for f in "DFLBR"]

    cd["D1"], cd["D2"], cd["D3"], cd["D4"], cd["D5"], cd["D6"], cd["D7"], cd["D8"], cd["D9"] = \
        cd["D7"], cd["D4"], cd["D1"], cd["D8"], cd["D5"], cd["D2"], cd["D9"], cd["D6"], cd["D3"]

    temp_f = [cf[f"F{i}"] for i in range(7, 10)]
    temp_r = [cr[f"R{i}"] for i in range(7, 10)]
    temp_b = [cb[f"B{i}"] for i in range(7, 10)]
    temp_l = [cl[f"L{i}"] for i in range(7, 10)]

    cf["F7"], cf["F8"], cf["F9"] = temp_l
    cr["R7"], cr["R8"], cr["R9"] = temp_f
    cb["B7"], cb["B8"], cb["B9"] = temp_r
    cl["L7"], cl["L8"], cl["L9"] = temp_b

def update_stickers_after_L(cubelets_by_face):
    cl, cu, cf, cd, cb = [cubelets_by_face[f] for f in "LUFDB"]

    cl["L1"], cl["L2"], cl["L3"], cl["L4"], cl["L5"], cl["L6"], cl["L7"], cl["L8"], cl["L9"] = \
        cl["L7"], cl["L4"], cl["L1"], cl["L8"], cl["L5"], cl["L2"], cl["L9"], cl["L6"], cl["L3"]

    temp_u = [cu["U1"], cu["U4"], cu["U7"]]
    temp_f = [cf["F1"], cf["F4"], cf["F7"]]
    temp_d = [cd["D1"], cd["D4"], cd["D7"]]
    temp_b = [cb["B3"], cb["B6"], cb["B9"]]

    cu["U1"], cu["U4"], cu["U7"] = temp_b
    cf["F1"], cf["F4"], cf["F7"] = temp_u
    cd["D1"], cd["D4"], cd["D7"] = temp_f
    cb["B3"], cb["B6"], cb["B9"] = temp_d

def update_stickers_after_R(cubelets_by_face):
    cr, cu, cf, cd, cb = [cubelets_by_face[f] for f in "RUFDB"]

    cr["R1"], cr["R2"], cr["R3"], cr["R4"], cr["R5"], cr["R6"], cr["R7"], cr["R8"], cr["R9"] = \
        cr["R7"], cr["R4"], cr["R1"], cr["R8"], cr["R5"], cr["R2"], cr["R9"], cr["R6"], cr["R3"]

    temp_u = [cu["U3"], cu["U6"], cu["U9"]]
    temp_f = [cf["F3"], cf["F6"], cf["F9"]]
    temp_d = [cd["D3"], cd["D6"], cd["D9"]]
    temp_b = [cb["B1"], cb["B4"], cb["B7"]]

    cu["U3"], cu["U6"], cu["U9"] = temp_f
    cf["F3"], cf["F6"], cf["F9"] = temp_d
    cd["D3"], cd["D6"], cd["D9"] = temp_b
    cb["B1"], cb["B4"], cb["B7"] = temp_u

def update_stickers_after_F(cubelets_by_face):
    cf, cu, cl, cd, cr = [cubelets_by_face[f] for f in "FULDR"]

    cf["F1"], cf["F2"], cf["F3"], cf["F4"], cf["F5"], cf["F6"], cf["F7"], cf["F8"], cf["F9"] = \
        cf["F7"], cf["F4"], cf["F1"], cf["F8"], cf["F5"], cf["F2"], cf["F9"], cf["F6"], cf["F3"]

    temp_u = [cu["U7"], cu["U8"], cu["U9"]]
    temp_l = [cl["L3"], cl["L6"], cl["L9"]]
    temp_d = [cd["D1"], cd["D2"], cd["D3"]]
    temp_r = [cr["R1"], cr["R4"], cr["R7"]]

    cu["U7"], cu["U8"], cu["U9"] = temp_l
    cl["L3"], cl["L6"], cl["L9"] = temp_d
    cd["D1"], cd["D2"], cd["D3"] = temp_r
    cr["R1"], cr["R4"], cr["R7"] = temp_u

def update_stickers_after_B(cubelets_by_face):
    cb, cu, cl, cd, cr = [cubelets_by_face[f] for f in "BULDR"]

    cb["B1"], cb["B2"], cb["B3"], cb["B4"], cb["B5"], cb["B6"], cb["B7"], cb["B8"], cb["B9"] = \
        cb["B7"], cb["B4"], cb["B1"], cb["B8"], cb["B5"], cb["B2"], cb["B9"], cb["B6"], cb["B3"]

    temp_u = [cu["U1"], cu["U2"], cu["U3"]]
    temp_l = [cl["L1"], cl["L4"], cl["L7"]]
    temp_d = [cd["D9"], cd["D8"], cd["D7"]]
    temp_r = [cr["R3"], cr["R6"], cr["R9"]]

    cu["U1"], cu["U2"], cu["U3"] = temp_r
    cr["R3"], cr["R6"], cr["R9"] = temp_d
    cd["D9"], cd["D8"], cd["D7"] = temp_l
    cl["L1"], cl["L4"], cl["L7"] = temp_u

#----------------------------------------------------------------------

cubelets_by_face = {face: {} for face in ["F", "U", "L", "B", "D", "R"]}

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


def get_face_cubes(face):
    cbf = cubelets_by_face
    if face == "F":
        return [cbf["F"][f"F{i}"] for i in range(1, 10)] + \
               [cbf["U"][f"U{i}"] for i in range(7, 10)] + \
               [cbf["D"][f"D{i}"] for i in range(1, 4)] + \
               [cbf["R"][f"R{i}"] for i in range(1, 10, 3)] + \
               [cbf["L"][f"L{i}"] for i in range(3, 10, 3)]
    elif face == "B":
        return [cbf["B"][f"B{i}"] for i in range(1, 10)] + \
               [cbf["U"][f"U{i}"] for i in range(1, 4)] + \
               [cbf["D"][f"D{i}"] for i in range(7, 10)] + \
               [cbf["R"][f"R{i}"] for i in range(3, 10, 3)] + \
               [cbf["L"][f"L{i}"] for i in range(1, 10, 3)]
    elif face == "U":
        return [cbf["U"][f"U{i}"] for i in range(1, 10)] + \
               [cbf["F"][f"F{i}"] for i in range(1, 4)] + \
               [cbf["R"][f"R{i}"] for i in range(1, 4)] + \
               [cbf["B"][f"B{i}"] for i in range(1, 4)] + \
               [cbf["L"][f"L{i}"] for i in range(1, 4)]
    elif face == "D":
        return [cbf["D"][f"D{i}"] for i in range(1, 10)] + \
               [cbf["F"][f"F{i}"] for i in range(7, 10)] + \
               [cbf["R"][f"R{i}"] for i in range(7, 10)] + \
               [cbf["B"][f"B{i}"] for i in range(7, 10)] + \
               [cbf["L"][f"L{i}"] for i in range(7, 10)]
    elif face == "L":
        return [cbf["L"][f"L{i}"] for i in range(1, 10)] + \
               [cbf["U"][f"U{i}"] for i in range(1, 10, 3)] + \
               [cbf["F"][f"F{i}"] for i in range(1, 10, 3)] + \
               [cbf["D"][f"D{i}"] for i in range(1, 10, 3)] + \
               [cbf["B"][f"B{i}"] for i in range(3, 10, 3)]
    elif face == "R":
        return [cbf["R"][f"R{i}"] for i in range(1, 10)] + \
               [cbf["U"][f"U{i}"] for i in range(3, 10, 3)] + \
               [cbf["F"][f"F{i}"] for i in range(3, 10, 3)] + \
               [cbf["D"][f"D{i}"] for i in range(3, 10, 3)] + \
               [cbf["B"][f"B{i}"] for i in range(1, 10, 3)]


animation_in_progress = False

def rotate_face(face):
    global animation_in_progress
    if animation_in_progress:
        return

    animation_in_progress = True

    face_cubes = get_face_cubes(face)

    # De-duplicate to avoid double-rotation
    # seen = set()
    # unique_cubes = []
    # for cube in face_cubes:
    #     if id(cube) not in seen:
    #         unique_cubes.append(cube)
    #         seen.add(id(cube))

    axis = axis_vectors[face]
    total_angle = radians(90)
    steps = 300
    dtheta = total_angle / steps

    for _ in range(steps):
        rate(60)
        for cube in face_cubes:
            cube.rotate(angle=-dtheta, axis=axis, origin=cube_center)

    # Update logical cubelets
    if face == "U": update_stickers_after_U(cubelets_by_face) , print("U face updated")

    elif face == "D": update_stickers_after_D(cubelets_by_face) , print("D face updated")
    elif face == "L": update_stickers_after_L(cubelets_by_face) , print("L face updated")
    elif face == "R": update_stickers_after_R(cubelets_by_face) , print("R face updated")
    elif face == "F": update_stickers_after_F(cubelets_by_face) , print("F face updated")
    elif face == "B": update_stickers_after_B(cubelets_by_face) , print("B face updated")

    animation_in_progress = False
    
      # Inside rotate_face() after sticker updates:
    print(f"After {face} rotation:")
    print("F1 color:", cubelets_by_face["F"]["F1"].color)
    print("U9 color:", cubelets_by_face["U"]["U9"].color)
    print("R3 color:", cubelets_by_face["R"]["R3"].color)

def key_pressed(evt):
    global animation_in_progress
    if animation_in_progress:
        return  # Ignore input while animating

    keyname = evt.key.upper()
    # Map keys to faces as before
    if keyname == 'J': keyname = 'U'
    elif keyname == 'S': keyname = 'D'
    elif keyname == 'H': keyname = 'F'
    elif keyname == 'W': keyname = 'B'
    elif keyname == 'D': keyname = 'L'
    elif keyname == 'K': keyname = 'R'

    if keyname in axis_vectors:
        rotate_face(keyname)

cubelets_by_face["F"]["F1"].color = color.cyan
cubelets_by_face["U"]["U9"].color = color.purple
cubelets_by_face["R"]["R3"].color = color.magenta

scene.bind('keydown', key_pressed)

# Keep the window open
while True:
    rate(60)  # Limit the loop to 60 iterations per second
    # This keeps the window responsive and allows for key events to be processed