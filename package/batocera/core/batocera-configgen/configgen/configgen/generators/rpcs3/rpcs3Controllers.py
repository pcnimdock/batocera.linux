import os
import batoceraFiles
from os import path
import codecs
from utils.logger import get_logger

eslog = get_logger(__name__)

rpcs3_input_dir = batoceraFiles.CONF + "/rpcs3/input_configs/global"

def generateControllerConfig(system, controllers, rom):
    if not path.isdir(rpcs3_input_dir):
        os.makedirs(rpcs3_input_dir)
    configFileName = f"{rpcs3_input_dir}/Default.yml"
    f = codecs.open(configFileName, "w", encoding="utf_8_sig")

    nplayer = 1
    for controller, pad in sorted(controllers.items()):
        if nplayer <= 7:
            f.write(f"Player {nplayer} Input:\n")
            f.write("  Handler: Evdev\n")
            f.write(f"  Device: {pad.dev}\n")
            f.write("  Config:\n")
            f.write("    Left Stick Left: LX-\n")
            f.write("    Left Stick Down: LY+\n")
            f.write("    Left Stick Right: LX+\n")
            f.write("    Left Stick Up: LY-\n")
            f.write("    Right Stick Left: RX-\n")
            f.write("    Right Stick Down: RY+\n")
            f.write("    Right Stick Right: RX+\n")
            f.write("    Right Stick Up: RY-\n")
            f.write("    Start: Start\n")
            f.write("    Select: Select\n")
            f.write("    PS Button: 0\n")
            f.write("    Square: Y\n")
            f.write("    Cross: A\n")
            f.write("    Circle: B\n")
            f.write("    Triangle: X\n")
            f.write("    Left: Hat0 X-\n")
            f.write("    Down: Hat0 Y+\n")
            f.write("    Right: Hat0 X+\n")
            f.write("    Up: Hat0 Y-\n")
            f.write("    R1: TR\n")
            f.write("    R2: TR 2\n")
            f.write("    R3: Thumb R\n")
            f.write("    L1: TL\n")
            f.write("    L2: TL 2\n")
            f.write("    L3: Thumb L\n")
            f.write("    Motion Sensor X:\n")
            f.write("      Axis: X\n")
            f.write("      Mirrored: false\n")
            f.write("      Shift: 0\n")
            f.write("    Motion Sensor Y:\n")
            f.write("      Axis: Y\n")
            f.write("      Mirrored: false\n")
            f.write("      Shift: 0\n")
            f.write("    Motion Sensor Z:\n")
            f.write("      Axis: Z\n")
            f.write("      Mirrored: false\n")
            f.write("      Shift: 0\n")
            f.write("    Motion Sensor G:\n")
            f.write("      Axis: RY\n")
            f.write("      Mirrored: false\n")
            f.write("      Shift: 0\n")
            f.write("    Pressure Intensity Button: ""\n")
            f.write("    Pressure Intensity Percent: 50\n")
            f.write("    Pressure Intensity Toggle Mode: false\n")
            f.write("    Left Stick Multiplier: 100\n")
            f.write("    Right Stick Multiplier: 100\n")
            f.write("    Left Stick Deadzone: 30\n")
            f.write("    Right Stick Deadzone: 30\n")
            f.write("    Left Trigger Threshold: 0\n")
            f.write("    Right Trigger Threshold: 0\n")
            f.write("    Left Pad Squircling Factor: 5000\n")
            f.write("    Right Pad Squircling Factor: 5000\n")
            f.write("    Color Value R: 0\n")
            f.write("    Color Value G: 0\n")
            f.write("    Color Value B: 20\n")
            f.write("    Blink LED when battery is below 20%: true\n")
            f.write("    Use LED as a battery indicator: false\n")
            f.write("    LED battery indicator brightness: 10\n")
            f.write("    Enable Large Vibration Motor: true\n")
            f.write("    Enable Small Vibration Motor: true\n")
            f.write("    Switch Vibration Motors: false\n")
            f.write("    Mouse Movement Mode: Relative\n")
            f.write("    Mouse Deadzone X Axis: 60\n")
            f.write("    Mouse Deadzone Y Axis: 60\n")
            f.write("    Mouse Acceleration X Axis: 200\n")
            f.write("    Mouse Acceleration Y Axis: 250\n")
            f.write("    Left Stick Lerp Factor: 100\n")
            f.write("    Right Stick Lerp Factor: 100\n")
            f.write("    Analog Button Lerp Factor: 100\n")
            f.write("    Trigger Lerp Factor: 100\n")
            f.write("    Device Class Type: 0\n")
            f.write("    Vendor ID: 1356\n")
            f.write("    Product ID: 616\n")
            f.write('  Buddy Device: "Null"\n')
        nplayer += 1
    f.close()
