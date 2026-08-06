import cv2
import numpy as np
import random
import time

# -----------------------------
# CONFIGURATION
# -----------------------------
IMAGE_PATH = "ayyappa_swamy.png"

DISPLAY_WIDTH = 550
DISPLAY_HEIGHT = 600

DRAW_TIME = 12        # seconds
FPS = 60              # frames per second

# -----------------------------
# LOAD IMAGE
# -----------------------------
img = cv2.imread(IMAGE_PATH)

if img is None:
    raise FileNotFoundError(f"Image not found: {IMAGE_PATH}")

img = cv2.resize(img, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

height, width = img.shape[:2]

# Black canvas
canvas = np.zeros_like(img)

# -----------------------------
# RANDOM PIXEL ORDER
# -----------------------------
coords = [(x, y) for y in range(height) for x in range(width)]
random.shuffle(coords)

total_pixels = len(coords)
total_frames = DRAW_TIME * FPS
pixels_per_frame = total_pixels // total_frames

cv2.namedWindow("Lord Ayyappa", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Lord Ayyappa", DISPLAY_WIDTH, DISPLAY_HEIGHT)

index = 0
start = time.time()

while True:

    # Draw pixels for this frame
    end = min(index + pixels_per_frame, total_pixels)

    for i in range(index, end):
        x, y = coords[i]
        canvas[y, x] = img[y, x]

    index = end

    cv2.imshow("Lord Ayyappa", canvas)

    if cv2.waitKey(1) & 0xFF == 27:   # ESC key
        break

    if index >= total_pixels:
        break

    # Maintain 60 FPS
    elapsed = time.time() - start
    expected = index / total_pixels * DRAW_TIME

    if expected > elapsed:
        time.sleep(expected - elapsed)

# Show final image
cv2.imshow("Lord Ayyappa", img)
cv2.waitKey(0)
cv2.destroyAllWindows()