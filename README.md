# AI-Arduino-Aimbot

AI-Arduino-Aimbot is a custom aimbot solution using a combination of AI (specifically YOLO for object detection) and Arduino for precise mouse control. It captures the screen, processes it through a trained AI model (PyTorch format), and uses Arduino to control the mouse cursor, simulating an aimbot functionality.

This project is ideal for integrating AI-powered aimbot functionality into your system, where the AI model can track and target specific objects on the screen, and the Arduino handles the mouse movements and actions.

## Features
- **AI-Powered Target Tracking**: Uses a YOLO model for object detection.
- **Arduino Mouse Control**: Arduino is used to move the mouse based on detected targets.
- **Customizable Control**: You can modify the mouse movement, smoothing, and target detection settings to suit your needs.
- **Silent Aimbot**: Includes functionality for silent aimbot (no visible cursor movement).
- **Cross-platform**: Works on Windows, Linux, or any OS that supports Python and Arduino.

## Requirements

### Hardware
- **Arduino Board** (e.g., Arduino Leonardo or Micro with USB HID support).
- **PC/Laptop** for running the Python script and controlling the game.

### Software
- **Python 3.x**
- **OpenCV**
- **mss** (for screen capture)
- **Ultralytics YOLO model** (for target detection)
- **keyboard library** (for keyboard input handling)

### Libraries and Dependencies
You can install the required libraries using `pip`:

```bash
pip install opencv-python mss ultralytics keyboard numpy colorama
```
### Usage
```bash
python sss.py --vid <Arduino VID> --pid <Arduino PID> --pcode <Ping Code from your Arduino Firmware>
```
### License
This project is licensed under the MIT License.
