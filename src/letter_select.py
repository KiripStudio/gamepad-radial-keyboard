import time
import math
from gamepad import Gamepad

DEADZONE = 0.3

GROUPS = {
    "UP":        ["E", "T", "A"],
    "UP_RIGHT":  ["O", "I", "N"],
    "RIGHT":     ["S", "H", "R"],
    "DOWN_RIGHT":["D", "L", "C"],
    "DOWN":      ["U", "M", "W"],
    "DOWN_LEFT": ["F", "G", "Y"],
    "LEFT":      ["P", "B", "V"],
    "UP_LEFT":   ["K", "J", "X", "Q"],
}


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
    js = pad.js
    
    selected_group = None
    waiting_for_release = False

    print("⌨️ Letter select ready")

    while True:
        pad.update()

        x = js.get_axis(0)
        y = js.get_axis(1)
        direction = get_direction(x, y)

        rt = pad.rt_pressed()

        # čekání na puštění RT
        if waiting_for_release:
            if not pad._axis_pressed(pad.RT_AXIS):
                waiting_for_release = False

        # 1️⃣ výběr skupiny
        elif rt and selected_group is None and direction:
            selected_group = direction
            waiting_for_release = True
            print(f"[GROUP] {direction} → {GROUPS[direction]}")

        # 2️⃣ výběr písmene
        elif rt and selected_group and direction:
            letters = GROUPS[selected_group]
            index = [
                "RIGHT", "UP_RIGHT", "UP", "UP_LEFT",
                "LEFT", "DOWN_LEFT", "DOWN", "DOWN_RIGHT"
            ].index(direction)

            letter = letters[index % len(letters)]
            print(f"[TYPE] {letter}")

            selected_group = None
            waiting_for_release = True

        time.sleep(0.05)
if __name__ == "__main__":
    main()