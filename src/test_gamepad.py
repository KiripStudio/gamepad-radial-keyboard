import time
from gamepad import Gamepad

pad = Gamepad()

print("🎮 Gamepad ready")

while True:
    pad.update()

    if pad.rt_pressed():
        print("RT PRESSED")

    if pad.lt_pressed():
        print("LT PRESSED")

    if pad.b_pressed():
        print("B PRESSED")

    if pad.lb_pressed():
        print("LB PRESSED")

    if pad.rb_pressed():
        print("RB PRESSED")

    time.sleep(0.05)