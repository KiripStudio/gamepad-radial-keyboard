import pygame
import math
import time

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
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("❌ No gamepad detected")
        return

    js = pygame.joystick.Joystick(0)
    js.init()

    print(f"🎮 Gamepad connected: {js.get_name()}")

    last_dir = None

    while True:
        pygame.event.pump()

        x = js.get_axis(0)   # left stick X
        y = js.get_axis(1)   # left stick Y

        direction = get_direction(x, y)

        if direction != last_dir:
            print(direction)
            last_dir = direction

        time.sleep(0.05)


if __name__ == "__main__":
    main()