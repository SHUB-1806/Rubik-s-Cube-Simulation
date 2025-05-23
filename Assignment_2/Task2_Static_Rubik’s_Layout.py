from vpython import *

# Create a scene
scene = canvas(title='Static Rubik\'s Cube', width=800, height=600, background=color.white)

size = vector(0.98, 0.98, 0.98)  # Size of each cubelet

for i in range(3):
    for j in range(3):
        for k in range(3):
            y = j - 1
            if(y == 1):
                cube = box(pos=vector(i, y, k), size= size, color=color.orange)
            
            elif(y == 0):
                cube = box(pos=vector(i, y, k), size= size, color=color.white)
            
            else:
                cube = box(pos=vector(i, y, k), size= size, color=color.green)
            
            

while True:
    rate(60) 