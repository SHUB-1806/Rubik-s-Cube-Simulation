# # Interactive 3D Rubik's Cube Simulator
# # VPython Implementation for Programming Assignment

# from vpython import *
# import math

# # Global variables
# cubes = []  # Array to store all 27 cube objects
# rotating = False  # Flag to prevent overlapping rotations
# rotation_axis = vector(0, 0, 0)
# rotation_center = vector(0, 0, 0)
# face_cubes = []  # Cubes in the currently rotating face

# # Face mapping - maps each face to the indices of cubes belonging to that face
# # Using 3x3x3 grid indexing: index = x + y*3 + z*9
# def get_cube_index(x, y, z):
#     """Convert 3D coordinates to linear index"""
#     return x + y*3 + z*9

# def get_cube_coords(index):
#     """Convert linear index to 3D coordinates"""
#     z = index // 9
#     y = (index % 9) // 3
#     x = index % 3
#     return x, y, z

# def create_cube_grid():
#     """Create the 3x3x3 grid of cubes"""
#     global cubes
#     cubes = []
    
#     # Create 27 cubes in a 3x3x3 arrangement
#     for z in range(3):
#         for y in range(3):
#             for x in range(3):
#                 # Position calculation: center cube at origin, 20 units spacing
#                 pos_x = (x - 1) * 20
#                 pos_y = (y - 1) * 20
#                 pos_z = (z - 1) * 20
                
#                 # Create cube with specified properties
#                 cube = box(
#                     pos=vector(pos_x, pos_y, pos_z),
#                     size=vector(19, 19, 19),
#                     color=color.white
#                 )
#                 cubes.append(cube)

# def get_face_cubes(face):
#     """Get list of cube indices belonging to a specific face"""
#     face_indices = []
    
#     if face == "front":  # z = 2 (front face)
#         for y in range(3):
#             for x in range(3):
#                 face_indices.append(get_cube_index(x, y, 2))
#     elif face == "back":  # z = 0 (back face)
#         for y in range(3):
#             for x in range(3):
#                 face_indices.append(get_cube_index(x, y, 0))
#     elif face == "right":  # x = 2 (right face)
#         for y in range(3):
#             for z in range(3):
#                 face_indices.append(get_cube_index(2, y, z))
#     elif face == "left":  # x = 0 (left face)
#         for y in range(3):
#             for z in range(3):
#                 face_indices.append(get_cube_index(0, y, z))
#     elif face == "up":  # y = 2 (top face)
#         for z in range(3):
#             for x in range(3):
#                 face_indices.append(get_cube_index(x, 2, z))
#     elif face == "down":  # y = 0 (bottom face)
#         for z in range(3):
#             for x in range(3):
#                 face_indices.append(get_cube_index(x, 0, z))
    
#     return face_indices

# def rotate_face(face):
#     """Rotate a face of the cube by 90 degrees clockwise"""
#     global rotating, rotation_axis, rotation_center, face_cubes
    
#     if rotating:
#         return  # Prevent overlapping rotations
    
#     rotating = True
#     face_indices = get_face_cubes(face)
#     face_cubes = [cubes[i] for i in face_indices]
    
#     # Set rotation parameters based on face
#     if face == "front":
#         rotation_axis = vector(0, 0, 1)
#         rotation_center = vector(0, 0, 20)
#     elif face == "back":
#         rotation_axis = vector(0, 0, -1)
#         rotation_center = vector(0, 0, -20)
#     elif face == "right":
#         rotation_axis = vector(1, 0, 0)
#         rotation_center = vector(20, 0, 0)
#     elif face == "left":
#         rotation_axis = vector(-1, 0, 0)
#         rotation_center = vector(-20, 0, 0)
#     elif face == "up":
#         rotation_axis = vector(0, 1, 0)
#         rotation_center = vector(0, 20, 0)
#     elif face == "down":
#         rotation_axis = vector(0, -1, 0)
#         rotation_center = vector(0, -20, 0)
    
#     # Perform smooth 90-degree rotation
#     angle_per_step = math.radians(1)  # 1 degree per step
#     total_steps = 90
    
#     for step in range(total_steps):
#         rate(60)  # 60 FPS animation
        
#         # Rotate each cube in the face
#         for cube in face_cubes:
#             cube.rotate(
#                 axis=rotation_axis,
#                 angle=angle_per_step,
#                 origin=rotation_center
#             )
    
#     rotating = False

# def handle_keyboard(evt):
#     """Handle keyboard input for face rotations"""
#     key = evt.key.lower()
    
#     # Map keys to face rotations according to assignment specification
#     if key == 'j':  # Rotate top face clockwise
#         rotate_face("up")
#     elif key == 's':  # Rotate bottom face clockwise
#         rotate_face("down")
#     elif key == 'h':  # Rotate front face clockwise
#         rotate_face("front")
#     elif key == 'w':  # Rotate back face clockwise
#         rotate_face("back")
#     elif key == 'd':  # Rotate left face clockwise
#         rotate_face("left")
#     elif key == 'k':  # Rotate right face clockwise
#         rotate_face("right")

# # Main program
# def main():
#     # Set up the VPython scene
#     scene.title = "Interactive 3D Rubik's Cube Simulator"
#     scene.width = 800
#     scene.height = 600
#     scene.background = color.black
#     scene.center = vector(0, 0, 0)
#     scene.range = 60
    
#     # Create instruction label
#     instructions = """Controls:
# J - Rotate top face clockwise
# S - Rotate bottom face clockwise  
# H - Rotate front face clockwise
# W - Rotate back face clockwise
# D - Rotate left face clockwise
# K - Rotate right face clockwise

# Note: Only one face can rotate at a time"""
    
#     label(pos=vector(0, -50, 0), text=instructions, 
#           color=color.white, height=12, align='center')
    
#     # Create the cube grid
#     create_cube_grid()
    
#     # Bind keyboard events
#     scene.bind('keydown', handle_keyboard)
    
#     # Main loop to keep program running
#     while True:
#         rate(60)

# # Run the program
# if __name__ == "__main__":
#     main()

from vpython import *
box()  # we need an object to get a canvas

def key_pressed(evt):  # info about event is stored in evt
    keyname = evt.key
    print('The ' + keyname + ' key was pressed.')

scene.bind('keydown', key_pressed)

while True:
    rate(60)  # run at 60 frames per second
    # The program will keep running, waiting for key presses
    # You can add more functionality here if needed