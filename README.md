# AI-Arduino-Aimbot

AI-Arduino-Aimbot is a custom aimbot solution using a combination of AI (specifically YOLO for object detection) and Arduino for precise mouse control. It captures the screen, processes it through a trained AI model (ONNX format), and uses Arduino to control the mouse cursor, simulating an aimbot functionality.

This project is ideal for integrating AI-powered aimbot functionality into your system, where the AI model can track and target specific objects on the screen, and the Arduino handles the mouse movements and actions.

Features
AI-Powered Target Tracking: Uses a YOLO model for object detection.
Arduino Mouse Control: Arduino is used to move the mouse based on detected targets.
Customizable Control: You can modify the mouse movement, smoothing, and target detection settings to suit your needs.
Silent Aimbot: Includes functionality for silent aimbot (no visible cursor movement).
Cross-platform: Works on Windows, Linux, or any OS that supports Python and Arduino.
Requirements
Hardware
Arduino Board (e.g., Arduino Leonardo or Micro with USB HID support).
PC/Laptop for running the Python script and controlling the game.
Software
Python 3.x
OpenCV
mss (for screen capture)
ONNX Runtime
Ultralytics YOLO model (for target detection)
keyboard library (for keyboard input handling)
Libraries and Dependencies
You can install the required libraries using pip:

bash
Copy code
pip install opencv-python mss onnxruntime keyboard numpy colorama
pip install ultralytics  # If using YOLO
Installation
Clone the Repository:

Clone the repository to your local machine.

bash
Copy code
git clone https://github.com/robertib24/AI-Arduino-Aimbot.git
cd AI-Arduino-Aimbot
Arduino Setup:

Upload the Arduino HID code to your Arduino board (like Arduino Leonardo or Micro) using the Arduino IDE.
Make sure your Arduino is configured correctly to send mouse movement commands.
Model Setup:

Download or train a YOLO model for your specific game or use case. The default code assumes an ONNX format model.
Place the model file (best.onnx) in the project directory, or modify the path in the code accordingly.
Configure Parameters:

Use the provided --vid, --pid, and --pcode options to specify your Arduino's Vendor ID, Product ID, and Pingcode.
If your Arduino is connected correctly, these parameters allow the Python script to communicate with it.
Run the Script:

Start the Python script:

bash
Copy code
python aimbot.py --vid <your_vid> --pid <your_pid> --pcode <your_pcode>
Replace <your_vid>, <your_pid>, and <your_pcode> with your Arduino's actual values.

Controls
Alt: Activate the aimbot. The mouse will follow the nearest detected target.
V: Activate silent aimbot, where the target movement is adjusted but less noticeable.
O: Exit the script.
How It Works
Screen Capture: The script continuously captures a region of the screen to process the video frames.
Object Detection: The captured frames are passed through a YOLO-based AI model to detect the targets (e.g., enemies or specific objects).
Mouse Control: Once a target is detected, the position is calculated, and Arduino moves the mouse cursor accordingly using HID commands.
Smoothing: The movement is smoothed using configurable smoothing factors to prevent erratic movements.
Customization
You can adjust several parameters:

Model Input Size: Modify the frame resizing logic to match the input size expected by your ONNX model.
Smoothing: Modify the SMOOTH_X and SMOOTH_Y constants to control the movement smoothness.
Bounding Box Processing: Adjust the object detection logic to handle different output formats or object types.
Troubleshooting
Arduino Not Detected: Ensure the Arduino board is correctly connected and the correct VID, PID, and Pingcode are set.
Performance Issues: If the frame rate or detection speed is low, consider optimizing the model or reducing the screen capture region.
License
This project is licensed under the MIT License - see the LICENSE file for details.
