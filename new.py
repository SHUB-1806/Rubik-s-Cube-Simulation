import cv2
import numpy as np


color_map = {
    1 : 'White',
    2 : 'Orange',
    3 : 'Green',
    4 : 'Red',
    5 : 'Blue',
    6 : 'Yellow'
}

def get_color():
    cap = cv2.VideoCapture(0)  # Change index if needed (e.g., 0 or 1)

    dot_x, dot_y = None, None
    alpha = 0.5
    square_size = 400
    circle_radius = 20

    color_bgr = []  # Will be a list of [B, G, R]
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        flip = cv2.flip(frame, 1)
        h, w = flip.shape[:2]
        if dot_x is None or dot_y is None:
            dot_x, dot_y = w // 2, h // 2

        overlay = flip.copy()
        top_left = (dot_x - square_size // 2, dot_y - square_size // 2)
        bottom_right = (dot_x + square_size // 2, dot_y + square_size // 2)

        cv2.rectangle(overlay, top_left, bottom_right, (0, 0, 0), 0)
        cv2.circle(overlay, (dot_x, dot_y), circle_radius, (0, 0, 0), 0)
        cv2.addWeighted(overlay, alpha, flip, 1 - alpha, 0, flip)

        cv2.putText(flip, f"Captured: {count}/6", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(flip, f"Color:"+color_map[count+1], (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Webcam - Press SPACE to capture BGR", flip)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            break
        elif key == 32:  # SPACE
            bgr = flip[dot_y, dot_x].tolist()  # Convert to [B, G, R]
            color_bgr.append(bgr)
            count += 1
            if count == 6:
                break

    cap.release()
    cv2.destroyAllWindows()

    return np.array(color_bgr, dtype=np.uint8)  


FACE_IDX = {
    'W': 0,  # Up
    'O': 1,  # Left
    'G': 2,  # Front
    'R': 3,  # Right
    'B': 4,  # Back
    'Y': 5   # Down
}
FACE_NAME = {v: k for k, v in FACE_IDX.items()}

def get_dot_positions(frame):
    """Return 9 sampling points in a 3×3 grid centered and aligned with square."""
    h, w = frame.shape[:2]
    gap = int(min(w, h) * 0.1)
    grid_w = 2 * gap
    grid_h = 2 * gap
    start_x = w // 2 - grid_w // 2
    start_y = h // 2 - grid_h // 2
    dots = [(start_x + j * gap, start_y + i * gap)
            for i in range(3) for j in range(3)]
    top_left = (start_x - gap // 2, start_y - gap // 2)
    bottom_right = (start_x + 2 * gap + gap // 2, start_y + 2 * gap + gap // 2)
    return dots, top_left, bottom_right

def classify_color(bgr, tol,COLOR_MAP):
    """Return label of closest color in COLOR_MAP within tolerance."""
    b, g, r = bgr
    for label, (ib, ig, ir) in COLOR_MAP.items():
        if (abs(b - ib) <= tol and
            abs(g - ig) <= tol and
            abs(r - ir) <= tol):
            return label
    return 'W'  # Unknown

def draw_grid(frame, face_colors,COLOR_MAP):
    """Draw the detected face_colors in a 3×3 block on the right."""
    cell = 40
    margin = 20
    top_left_x = frame.shape[1] - cell * 3 - margin
    top_left_y = margin

    for i in range(3):
        for j in range(3):
            code = face_colors[i*3+j]
            col = tuple(map(int, COLOR_MAP.get(code, (50, 50, 50))))
            x = top_left_x + j * cell
            y = top_left_y + i * cell
            cv2.rectangle(frame, (x, y), (x + cell, y + cell), col, -1)
            cv2.rectangle(frame, (x, y), (x + cell, y + cell), (0, 0, 0), 2)

def scan():
    color_bgr = get_color()
    COLOR_MAP = {
        'W': tuple(color_bgr[0]),  # White
        'O': tuple(color_bgr[1]),  # Orange
        'G': tuple(color_bgr[2]),  # Green
        'R': tuple(color_bgr[3]),  # Red
        'B': tuple(color_bgr[4]),  # Blue
        'Y': tuple(color_bgr[5])   # Yellow
    }
    cap = cv2.VideoCapture(0)
    faces_data = [None] * 6
    scanned_count = 0
    alpha = 1  # dot opacity

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip frame once
        flip = cv2.flip(frame, 1)
        overlay = flip.copy()

        # Get grid dot positions and square bounding box
        dots, top_left, bottom_right = get_dot_positions(flip)

        # Draw sampling dots on overlay
        for (x, y) in dots:
            cv2.circle(overlay, (x, y), 10, (0, 0, 0), 0)
        # Blend overlay and frame
        cv2.addWeighted(overlay, alpha, flip, 1 - alpha, 0, flip)

        # Sample colors from dot regions and classify
        face_colors = []
        for (x, y) in dots:
            roi = flip[y-5:y+5, x-5:x+5]
            if roi.size:
                avg = np.mean(roi, axis=(0, 1))
                face_colors.append(classify_color(avg ,50,COLOR_MAP))
            else:
                face_colors.append('K')

        # Draw face preview grid and scanning square
        draw_grid(flip, face_colors,COLOR_MAP)
        cv2.rectangle(flip, top_left, bottom_right, (0, 0, 0), 2)

        # Text
        cv2.putText(flip,
                    f"Scanned: {scanned_count}/6",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show frame
        cv2.imshow("Rubik's Face Detector", flip)

        # Handle key input
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            break
        elif key == 32:  # SPACE to store face
            center_code = face_colors[4]
            idx = FACE_IDX.get(center_code, None)
            if idx is None:
                print("⚠️  Center sticker unrecognized, try again.")
            elif faces_data[idx] is not None:
                print(f"⚠️  Face {FACE_NAME[idx]} already scanned.")
            else:
                faces_data[idx] = [face_colors[i*3:(i+1)*3][::-1] for i in range(3)]
                scanned_count += 1
                # print(f"✅  Stored face {FACE_NAME[idx]} at index {idx}")
                if scanned_count == 6:
                    print("\n🎉 All 6 faces scanned!")
                    # for i, face in enumerate(faces_data):
                    #     print(f"Face {i} ({FACE_NAME[i]}):")
                    #     for row in face:
                    #         print(" ", row)
                    break
        elif key == ord('d'):  # Press 'd' to print debug BGR averages
            print("🔍 Sampled BGR values:")
            for i, (x, y) in enumerate(dots):
                roi = flip[y-5:y+5, x-5:x+5]
                if roi.size:
                    avg = np.mean(roi, axis=(0, 1))
                    print(f"Dot {i}: {avg}")
    state = "".join(
        faces_data[f][r][c]
        for f in range(6)
        for r in range(3)
        for c in range(3)
    )
    cap.release()
    cv2.destroyAllWindows()
    return state  # this is an string of 54 letter 

if __name__ == "__main__":
    scan()