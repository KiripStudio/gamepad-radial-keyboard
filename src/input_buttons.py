import pygame
import time

AXIS_THRESHOLD = 0.5  # pro trigery jako osa


def main():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("❌ No gamepad detected")
        return

    js = pygame.joystick.Joystick(0)
    js.init()

    print(f"🎮 Gamepad connected: {js.get_name()}")
    print(f"Buttons: {js.get_numbuttons()}")
    print(f"Axes: {js.get_numaxes()}")
    print("-" * 40)

    last_buttons = [0] * js.get_numbuttons()
    last_axes = [0.0] * js.get_numaxes()

    while True:
        pygame.event.pump()

        # ---- BUTTONS ----
        for i in range(js.get_numbuttons()):
            state = js.get_button(i)
            if state != last_buttons[i]:
                print(f"BUTTON {i}: {'PRESSED' if state else 'RELEASED'}")
                last_buttons[i] = state

        # ---- AXES (triggers often here) ----
        for i in range(js.get_numaxes()):
            value = js.get_axis(i)

            if value > AXIS_THRESHOLD and last_axes[i] <= AXIS_THRESHOLD:
                print(f"AXIS {i}: PRESSED ({value:.2f})")

            if value <= AXIS_THRESHOLD and last_axes[i] > AXIS_THRESHOLD:
                print(f"AXIS {i}: RELEASED ({value:.2f})")

            last_axes[i] = value

        time.sleep(0.05)


if __name__ == "__main__":
    main()