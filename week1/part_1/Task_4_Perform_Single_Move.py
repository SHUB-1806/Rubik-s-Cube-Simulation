cube = {
    'U': [['B', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
    'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],
    'F': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
    'B': [['W', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
    'L': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
    'R': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
}

def print_cube_2D(cube):

    def face_row(face, row):
        return ''.join(cube[face][row])

    #printing U face
    for i in range(3):
        print(' ' * 6 + face_row('U', i))
    print("")

    # Printing L, F, R, B faces
    for i in range(3):
        print(
            face_row('L', i) + '   ' +
            face_row('F', i) + '   ' +
            face_row('R', i) + '   ' +
            face_row('B', i)
        )
    print("")

    # Printing D face
    for i in range(3):
        print(' ' * 6 + face_row('D', i))
    print("")

    
#     matrix = [[matrix[j][i] for j in range(3)] for i in range(3)] only rebinds the name matrix locally inside the function.
#     If you want to update the actual 2D list (like cube['U']), you must modify its contents directly.

def transpose(matrix):
    for i in range(3):
        for j in range(i+1, 3):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse_rows(matrix):
    for row in matrix:
        row.reverse()

def exchange_rows(matrix1, matrix2, nth_row):
    for i in range(3):
        matrix1[nth_row - 1][i], matrix2[nth_row - 1][i] = matrix2[nth_row - 1][i], matrix1[nth_row - 1][i]


def CW_rot(face):
    transpose(face)
    reverse_rows(face)

def ACW_rot(face):
    reverse_rows(face)
    transpose(face)

def perform_move_U(cube):

    #updating top face
    CW_rot(cube['U'])

    #updating F, R, B, L
    exchange_rows(cube['F'], cube['R'], 1)
    exchange_rows(cube['R'], cube['B'], 1)
    exchange_rows(cube['B'], cube['L'], 1)

def perform_move_U2(cube):
    perform_move_U(cube)
    perform_move_U(cube)

print("Original Cube Net")
print_cube_2D(cube)

perform_move_U(cube)
print("After performing U move")
print_cube_2D(cube)

perform_move_U2(cube)
print("After performing U2 move")
print_cube_2D(cube)