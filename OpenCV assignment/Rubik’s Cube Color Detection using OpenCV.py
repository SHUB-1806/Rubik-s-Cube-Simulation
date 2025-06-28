import cv2
import numpy as np

cap = cv2.VideoCapture(0)

reference_colors = {
    (76, 177, 110): "Green",
    (255, 170, 61): "Orange",
    (53, 97, 140): "Blue",
    (255, 105, 85): "Red",
    (222, 238, 248): "White",
    (247, 222, 95): "Yellow"
}

color_letter = {
    'Red': 'R',
    'Green': 'G',
    'Blue': 'B',
    'White': 'W',
    'Yellow': 'Y',
    'Orange': 'O'
}

standard_bgr = {
    "Red": (0, 0, 255),
    "Green": (0, 255, 0),
    "Blue": (255, 0, 0),
    "White": (255, 255, 255),
    "Yellow": (0, 255, 255),
    "Orange": (0, 128, 255)
}

def get_nearest_color_name(rgb):
    min_dist = float('inf')
    closest_name = None
    for ref_rgb, name in reference_colors.items():
        dist = np.linalg.norm(np.array(rgb) - np.array(ref_rgb))
        if dist < min_dist:
            min_dist = dist
            closest_name = name
    return closest_name

def draw_mini_face(frame, face_colors, top_left=None, cell_size=30):
    if top_left is None:
        top_left = (frame.shape[1] - 120, 20)
    for i in range(3):
        for j in range(3):
            color = face_colors[i][j]
            bgr = standard_bgr.get(color, (0, 0, 0))
            x = top_left[0] + j * cell_size
            y = top_left[1] + i * cell_size
            cv2.rectangle(frame, (x, y), (x + cell_size, y + cell_size), bgr, -1)
            cv2.rectangle(frame, (x, y), (x + cell_size, y + cell_size), (0, 0, 0), 1)

cube = {}
face_order = ['U', 'R', 'F', 'D', 'L', 'B']
current_face_index = 0
scanned_faces = 0
last_face = [["White"] * 3 for _ in range(3)]

ret, frame = cap.read()
frame_height, frame_width = frame.shape[:2]
square_size = 200
start_x = frame_width // 2 - square_size // 2
start_y = frame_height // 2 - square_size // 2
end_x = start_x + square_size
end_y = start_y + square_size

grid_points = []
for i in range(3):
    for j in range(3):
        x = start_x + (j + 0.5) * square_size // 3
        y = start_y + (i + 0.5) * square_size // 3
        grid_points.append((int(x), int(y)))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=10)

    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255, 255, 255), 2)
    for pt in grid_points:
        cv2.circle(frame, pt, 5, (255, 255, 255), 1)

    cv2.putText(frame, f"Scanned: {scanned_faces}/6", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if last_face:
        draw_mini_face(frame, last_face)

    cv2.imshow("Rubik's Cube Scanner", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

    elif key == 32 and current_face_index < 6:
        face_name = face_order[current_face_index]
        face_grid = []

        print(f"\n Scanning face '{face_name}':")

        for i in range(3):
            row = []
            for j in range(3):
                idx = i * 3 + j
                pt = grid_points[idx]
                bgr = frame[pt[1], pt[0]]
                rgb = tuple(int(c) for c in bgr[::-1])
                cname = get_nearest_color_name(rgb)
                print(f"  Sticker {i},{j}: RGB={rgb} -> {cname}")
                row.append(cname)
            face_grid.append(row)

        cube[face_name] = [[color_letter[c] for c in row] for row in face_grid]
        last_face = face_grid
        scanned_faces += 1
        current_face_index += 1
        print(f" Saved {face_name} face.")

cap.release()
cv2.destroyAllWindows()

def print_cube_2D(cube):
    def face_row(face, row):
        return ''.join(cube[face][row])
    for i in range(3):
        print(' ' * 6 + face_row('U', i))
    print("")
    for i in range(3):
        print(
            face_row('L', i) + '   ' +
            face_row('F', i) + '   ' +
            face_row('R', i) + '   ' +
            face_row('B', i)
        )
    print("")
    for i in range(3):
        print(' ' * 6 + face_row('D', i))

if scanned_faces == 6:
    print_cube_2D(cube)
