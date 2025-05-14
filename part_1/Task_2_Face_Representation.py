# R G B W W B Y R B
face = [[None for j in range(3)] for i in range(3)]
color_count = {'W':0, 'Y':0, 'R':0, 'O':0, 'B':0, 'G':0, }


def fill_the_face():
    elements = input().split()
    k = 0
    for i in range(3):
        for j in range(3):
            face[i][j] = elements[k]
            k += 1

def count_colors():
    for i in range(3):
        for j in range(3):
            color_count[face[i][j]] += 1

def is_valid_face():
    for key in color_count:
        if(color_count.get(key)==6):
            print("is a valid face")
            return
    print("is not a valid face")

#better use these functions to avoid using gllobal face which will be helpful in future when treating complete cube       
# def transpose(matrix):
#     for i in range(3):
#         for j in range(i+1, 3):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# def reverse_rows(matrix):
#     for row in matrix:
#         row.reverse()

def transpose():
    global face
    face = [[face[j][i] for j in range(3)] for i in range(3)]
    # print(trans)

def rev_row():
    global face
    face = [[face[i][j] for j in  range(2,-1,-1)] for i in range(3)]
    # print(rev)

def rotate_face_CW():
    transpose()
    rev_row()

def rotate_face_ACW():
    rev_row()
    transpose()




fill_the_face()
count_colors()
print(color_count)
is_valid_face()

print(face)

rotate_face_CW()
print(face)

rotate_face_CW()
rotate_face_CW()
rotate_face_CW()
print(face)







# Example dictionary