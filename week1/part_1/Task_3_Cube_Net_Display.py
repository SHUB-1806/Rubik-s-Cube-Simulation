cube = {
    'U': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
    'D': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],
    'F': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
    'B': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
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

print_cube_2D(cube)
