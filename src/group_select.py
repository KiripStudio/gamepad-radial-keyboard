import time
import math
from gamepad import Gamepad

DEADZONE = 0.3

def get_direction(x, y):
    if abs(x) < DEADZONE and abs(y) < DEADZONE:
        return None

    angle = math.degrees(math.atan2(-y, x)) % 360
    directions = [
        "RIGHT", "UP_RIGHT", "UP", "UP_LEFT",
        "LEFT", "DOWN_LEFT", "DOWN", "DOWN_RIGHT"
    ]
    return directions[int((angle + 22.5) // 45) % 8]


def main():
    pad = Gamepad()
    js = pad.js  # jen čtení os, logika zůstává v Gamepad

    print("🧭 Group select ready")

    current_dir = None

    while True:
        pad.update()

        x = js.get_axis(0)
        y = js.get_axis(1)

        direction = get_direction(x, y)

        if direction != current_dir:
            print("DIR:", direction)
            current_dir = direction

        if pad.rt_pressed() and direction:
            print(f"SELECTED GROUP: {direction}")

        time.sleep(0.05)


if __name__ == "__main__":
    main()