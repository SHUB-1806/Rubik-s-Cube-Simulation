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

face_dirs = {
    "U": vector(0, 1, 0),
    "D": vector(0, -1, 0),
    "F": vector(0, 0, 1),
    "B": vector(0, 0, -1),
    "L": vector(-1, 0, 0),
    "R": vector(1, 0, 0)
}

#initialising the cubelets

cubelets_by_face = {"F": {f"F{i}": [] for i in range(1, 10)}
                    , "R": {f"R{i}": [] for i in range(1, 10)}
                    , "B": {f"B{i}": [] for i in range(1, 10)}
                    , "L": {f"L{i}": [] for i in range(1, 10)}
                    , "U": {f"U{i}": [] for i in range(1, 10)}
                    , "D": {f"D{i}": [] for i in range(1, 10)}
                    }

#__________OR___________
# cubelets_by_face = {
#     "U" : {
#         "U1": [], "U2": [], "U3": [],
#         "U4": [], "U5": [], "U6": [],
#         "U7": [], "U8": [], "U9": []
#     },
#     "F" : {
#         "F1": [], "F2": [], "F3": [],
#         "F4": [], "F5": [], "F6": [],
#         "F7": [], "F8": [], "F9": []
#     },
#     "R" : {
#         "R1": [], "R2": [], "R3": [],
#         "R4": [], "R5": [], "R6": [],
#         "R7": [], "R8": [], "R9": []
#     },
#     "B" : {
#         "B1": [], "B2": [], "B3": [],
#         "B4": [], "B5": [], "B6": [],
#         "B7": [], "B8": [], "B9": []
#     },
#     "L" : {
#         "L1": [], "L2": [], "L3": [],
#         "L4": [], "L5": [], "L6": [],
#         "L7": [], "L8": [], "L9": []
#     },
#     "D" : {
#         "D1": [], "D2": [], "D3": [],
#         "D4": [], "D5": [], "D6": [],
#         "D7": [], "D8": [], "D9": []
#     },
# }

face_rotations = {
    "U_face_list" : [
        *[cubelets_by_face["U"][f"U{i}"] for i in range(1,10)],
        *[cubelets_by_face["F"][f"F{i}"] for i in range(1,4)],
        *[cubelets_by_face["R"][f"R{i}"] for i in range(1,4)],
        *[cubelets_by_face["L"][f"L{i}"] for i in range(1,4)],
        *[cubelets_by_face["B"][f"B{i}"] for i in range(1,4)]
    ]
    , "D_face_list" : [
        *[cubelets_by_face["D"][f"D{i}"] for i in range(1,10)],
        *[cubelets_by_face["F"][f"F{i}"] for i in range(7,10)],
        *[cubelets_by_face["R"][f"R{i}"] for i in range(7,10)],
        *[cubelets_by_face["L"][f"L{i}"] for i in range(7,10)],
        *[cubelets_by_face["B"][f"B{i}"] for i in range(7,10)]
    ]
    , "F_face_list" : [
        *[cubelets_by_face["F"][f"F{i}"] for i in range(1,10)],
        *[cubelets_by_face["U"][f"U{i}"] for i in range(7,10)],
        *[cubelets_by_face["R"][f"R{i}"] for i in range(1,4)],
        *[cubelets_by_face["L"][f"L{i}"] for i in range(7,10)],
        *[cubelets_by_face["D"][f"D{i}"] for i in range(1,4)]
    ]
    , "B_face_list" : [
        *[cubelets_by_face["B"][f"B{i}"] for i in range(1,10)],
        *[cubelets_by_face["U"][f"U{i}"] for i in range(1,4)],
        *[cubelets_by_face["R"][f"R{i}"] for i in range(7,10)],
        *[cubelets_by_face["L"][f"L{i}"] for i in range(1,4)],
        *[cubelets_by_face["B"][f"B{i}"] for i in range(7,10)]
    ]
    , "L_face_list" : [
        *[cubelets_by_face["L"][f"L{i}"] for i in range(1,10)],
        *[cubelets_by_face["U"][f"U{i}"] for i in range(1,4)],
        *[cubelets_by_face["F"][f"F{i}"] for i in range(7,10)],
        *[cubelets_by_face["B"][f"B{i}"] for i in range(1,4)],
        *[cubelets_by_face["L"][f"L{i}"] for i in range(1,4)]
    ]
    , "R_face_list" : [
        *[cubelets_by_face["R"][f"R{i}"] for i in range(1,10)],
        *[cubelets_by_face["U"][f"U{i}"] for i in range(7,10)],
        *[cubelets_by_face["F"][f"F{i}"] for i in range(1,4)],
        *[cubelets_by_face["B"][f"B{i}"] for i in range(7,10)],
        *[cubelets_by_face["R"][f"R{i}"] for i in range(1,4)]
    ]

}


# Front face
#__________this is simply this___________
# vec1 in [vector(-1,1,0), vector(0,1,0), vector(1,1,0), vector(-1,0,0), vector(0,0,0), vector(1,0,0), vector(-1,-1,0), vector(0,-1,0), vector(1,-1,0)]:
vec_F = [vector(i, j, 0) for i in range(-1, 2) for j in range(-1, 2)]
vec_U = [vector(i, 0, j) for i in range(-1, 2) for j in range(-1, 2)]
vec_L = [vector(0, i, j) for i in range(-1, 2) for j in range(-1, 2)]

#__________this is simply this___________
# vec1 in [vector(-1,1,0), vector(0,1,0), vector(1,1,0), vector(-1,0,0), vector(0,0,0), vector(1,0,0), vector(-1,-1,0), vector(0,-1,0), vector(1,-1,0)]:

#front face


for idx in range(9):
    key = "U" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["yellow"] + vec_U[idx],
                  size = vector(cubelet_length, thickness, cubelet_length),
                  color = color.yellow)
    cubelets_by_face["U"][key] = cubelet

for idx in range(9):
    key = "L" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["red"] + vec_L[idx],
                  size = vector(thickness, cubelet_length, cubelet_length),
                  color = color.red)
    cubelets_by_face["L"][key] = cubelet

for idx in range(9):
    key = "B" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["blue"] + vec_F[idx],
                  size = vector(cubelet_length, cubelet_length, thickness),
                  color = color.blue)
    cubelets_by_face["B"][key] = cubelet

for idx in range(9):
    key = "D" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["white"] + vec_U[idx],
                  size = vector(cubelet_length, thickness, cubelet_length),
                  color = color.white)
    cubelets_by_face["D"][key] = cubelet

for idx in range(9):
    key = "R" + str(idx + 1)
    cubelet = box(pos = cube_center + centre_position["orange"] + vec_L[idx],
                  size = vector(thickness, cubelet_length, cubelet_length),
                  color = color.orange)
    cubelets_by_face["R"][key] = cubelet


# Right face
# for vec1 in [vector(0,0,0), vector(0, 0, 1), vector(0, 0, -1), vector(0, 1, 0), vector(0, -1, 0), vector(0,1,1), vector(0, -1, -1), vector(0, 1, -1), vector(0, -1, 1)]:
#     right = box(pos =cube_center + centre_position["orange"] + vec1 , size=vector(thickness, cubelet_length, cubelet_length), color=color.orange)
#     cubelets_by_face["R"].append(right)

# # Back face
# for vec1 in [vector(0,0,0), vector(1, 0, 0), vector(-1, 0, 0), vector(0, 1, 0), vector(0, -1, 0), vector(1, 1, 0), vector(-1, -1, 0), vector(1, -1, 0), vector(-1, 1, 0)]:
#     back = box(pos =cube_center + centre_position["blue"] + vec1 , size=vector(cubelet_length, cubelet_length, thickness), color=color.blue)
#     cubelets_by_face["B"].append(back)

# # Left face
# for vec1 in [vector(0,0,0), vector(0, 0, 1), vector(0, 0, -1), vector(0, 1, 0), vector(0, -1, 0), vector(0,1,1), vector(0, -1, -1), vector(0, 1, -1), vector(0, -1, 1)]:
#     left = box(pos =cube_center + centre_position["red"] + vec1 , size=vector(thickness, cubelet_length, cubelet_length), color=color.red)
#     cubelets_by_face["L"].append(left)

# # Top face
# for vec1 in [vector(0,0,0), vector(1, 0, 0), vector(-1, 0, 0), vector(0, 0, 1), vector(0, 0, -1), vector(1, 0, 1), vector(-1, 0, -1), vector(1, 0, -1), vector(-1, 0, 1)]:
#     top = box(pos =cube_center + centre_position["yellow"] + vec1 , size=vector(cubelet_length, thickness, cubelet_length), color=color.yellow)
#     cubelets_by_face["U"].append(top)

# # Bottom face
# for vec1 in [vector(0,0,0), vector(1, 0, 0), vector(-1, 0, 0), vector(0, 0, 1), vector(0, 0, -1), vector(1, 0, 1), vector(-1, 0, -1), vector(1, 0, -1), vector(-1, 0, 1)]:
#     bottom = box(pos =cube_center + centre_position["white"] + vec1 , size=vector(cubelet_length, thickness, cubelet_length), color=color.white)
#     cubelets_by_face["D"].append(bottom)

# cubelets_by_face["F"].append(top.)


# === Keyboard Input ===
def key_input(evt):
    k = evt.key.upper()
    if k in face_dirs:
        rotate_face(k)

scene.bind('keydown', key_input)

def rotate_face(face):
    axis = face_dirs[face]
    angle = pi / 2  # 90 degrees in radians
    for items in face_rotations[f"{face}_face_list"]:
        items.rotate(angle=angle, axis=axis, origin=cube_center)

# Keep the window open
while True:
    rate(100)  # Limit the loop to 100 iterations per second
