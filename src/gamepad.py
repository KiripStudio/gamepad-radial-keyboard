import pygame

AXIS_THRESHOLD = 0.5

class Gamepad:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            raise RuntimeError("No gamepad detected")

        self.js = pygame.joystick.Joystick(0)
        self.js.init()

        # --- mapping (TVŮJ GAMEPAD) ---
        self.B_BUTTON = 1
        self.LB_BUTTON = 4
        self.RB_BUTTON = 5

        self.LT_AXIS = 4
        self.RT_AXIS = 5

        # --- previous state (edge detection) ---
        self._last = {
            "B": False,
            "LB": False,
            "RB": False,
            "LT": False,
            "RT": False,
        }

    def update(self):
        pygame.event.pump()

    # ---------- helpers ----------
    def _axis_pressed(self, axis_index):
        return self.js.get_axis(axis_index) > AXIS_THRESHOLD

    def _button_pressed(self, button_index):
        return self.js.get_button(button_index) == 1

    def _edge(self, name, current):
        last = self._last[name]
        self._last[name] = current
        return current and not last

    # ---------- public API ----------
    def rt_pressed(self):
        return self._edge("RT", self._axis_pressed(self.RT_AXIS))

    def lt_pressed(self):
        return self._edge("LT", self._axis_pressed(self.LT_AXIS))

    def b_pressed(self):
        return self._edge("B", self._button_pressed(self.B_BUTTON))

    def lb_pressed(self):
        return self._edge("LB", self._button_pressed(self.LB_BUTTON))

    def rb_pressed(self):
        return self._edge("RB", self._button_pressed(self.RB_BUTTON))