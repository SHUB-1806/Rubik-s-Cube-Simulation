from vpython import *
# Create a scene
scene = canvas(title='Rainbow Cube', width=800, height=600, background=color.white)
# Create a cube

centre_pos = {
    'front' : vector(0, 0, 1),
    'back' : vector(0, 0, -1),
    'left' : vector(-1,0, 0),
    'right' : vector(1, 0, 0),
    'top' : vector(0, 1, 0),
    'bottom' : vector(0, -1, 0)
}

face_colors = {
    'F' : color.green,
    'B' : color.blue,
    'R' : color.orange,
    'L' : color.red,
    'U' : color.yellow,
    'D' : color.white
}

length_of_sticker = 0.98
thickness_of_sticker = 0.02
cube_centre = vector(0, 0, 0)

#so that each sticker can be identified by its face and number
cubelets_by_face = {'F' : [f"F{i}" for i in range(1, 5)],
                    'R' : [f"R{i}" for i in range(1, 5)],
                    'B' : [f"B{i}" for i in range(1, 5)],
                    'L' : [f"L{i}" for i in range(1, 5)],
                    'U' : [f"U{i}" for i in range(1, 5)],
                    'D' : [f"D{i}" for i in range(1, 5)]
                    }

#front
for i in range(1, 5):
    key = "F" + str(i)
    vec1 = [vector(-0.5, 0.5, 0), vector(0.5, 0.5, 0), vector(-0.5, -0.5, 0), vector(0.5, -0.5, 0)]
    cubelet = box(pos= cube_centre + centre_pos['front'] + vec1[i-1], size=vector(length_of_sticker, length_of_sticker, thickness_of_sticker), color=face_colors['F'])
    cubelets_by_face[key] = cubelet

#back
for i in range(1, 5):
    key = "B" + str(i)
    vec1 = [vector(-0.5, 0.5, 0), vector(0.5, 0.5, 0), vector(-0.5, -0.5, 0), vector(0.5, -0.5, 0)]
    cubelet = box(pos= cube_centre + centre_pos['back'] + vec1[i-1], size=vector(length_of_sticker, length_of_sticker, thickness_of_sticker), color=face_colors['B'])
    cubelets_by_face[key] = cubelet

#left
for i in range(1, 5):
    key = "L" + str(i)
    vec1 = [vector(0, 0.5, -0.5), vector(0, 0.5, 0.5), vector(0, -0.5, -0.5), vector(0, -0.5, 0.5)]
    cubelet = box(pos= cube_centre + centre_pos['left'] + vec1[i-1], size=vector(thickness_of_sticker, length_of_sticker, length_of_sticker), color=face_colors['L'])
    cubelets_by_face[key] = cubelet

#right
for i in range(1, 5):
    key = "R" + str(i)
    vec1 = [vector(0, 0.5, -0.5), vector(0, 0.5, 0.5), vector(0, -0.5, -0.5), vector(0, -0.5, 0.5)]
    cubelet = box(pos= cube_centre + centre_pos['right'] + vec1[i-1], size=vector(thickness_of_sticker, length_of_sticker, length_of_sticker), color=face_colors['R'])
    cubelets_by_face[key] = cubelet

#top
for i in range(1, 5):
    key = "U" + str(i)
    vec1 = [vector(-0.5, 0, 0.5), vector(0.5, 0, 0.5), vector(-0.5, 0, -0.5), vector(0.5, 0, -0.5)]
    cubelet = box(pos= cube_centre + centre_pos['top'] + vec1[i-1], size=vector(length_of_sticker, thickness_of_sticker, length_of_sticker), color=face_colors['U'])
    cubelets_by_face[key] = cubelet

#bottom
for i in range(1, 5):
    key = "D" + str(i)
    vec1 = [vector(-0.5, 0, 0.5), vector(0.5, 0, 0.5), vector(-0.5, 0, -0.5), vector(0.5, 0, -0.5)]
    cubelet = box(pos= cube_centre + centre_pos['bottom'] + vec1[i-1], size=vector(length_of_sticker, thickness_of_sticker, length_of_sticker), color=face_colors['D'])
    cubelets_by_face[key] = cubelet


# print(cubelet.name)
while True:
    rate(60)
