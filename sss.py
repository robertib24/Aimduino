import time
import numpy as np
import keyboard
import argparse
import cv2
import mss

from colorama import Fore
from ultralytics import YOLO
from mouse_instruct import MouseInstruct

SMOOTH_X = 0.8
SMOOTH_Y = 0.8

class Game:
    def __init__(self, VID, PID, PING_CODE):
        # Use mss for screen capture
        self.sct = mss.mss()  # Screen capture
        self.mouse = MouseInstruct.getMouse(VID, PID, PING_CODE)
        self.model = YOLO('./best.pt').to('cuda')  # Run on CPU (slower) or CUDA as needed

    def get_xy(self):
        # Capture a portion of the screen
        monitor = {"top": 220, "left": 640, "width": 1280, "height": 860}
        screenshot = self.sct.grab(monitor)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)  # Convert to RGB

        dx, dy = None, None
        if frame is None:
            return dx, dy

        # Run YOLO prediction (frame as input)
        results = self.model.predict(frame, verbose=False, conf=0.45)

        if results and len(results) > 0:
            boxes = results[0].boxes.xyxy.cpu().numpy()
            scores = results[0].boxes.conf.cpu().numpy()

            # Apply OpenCV's NMS
            indices = cv2.dnn.NMSBoxes(
                boxes.tolist(),  # List of boxes as [x1, y1, x2, y2]
                scores.tolist(),  # Confidence scores for each box
                score_threshold=0.45,  # Confidence threshold
                nms_threshold=0.4  # IoU threshold for NMS
            )

            # If we have detections after NMS, process them
            if len(indices) > 0:
                min_dist = float('inf')
                center_x, center_y = 320, 320  # Center of the frame

                # Find the closest enemy based on Euclidean distance
                for idx in indices.flatten():
                    x1, y1, x2, y2 = boxes[idx]
                    enemy_center_x = (x1 + x2) / 2
                    enemy_center_y = (y1 + y2) / 2

                    tx = enemy_center_x - center_x
                    ty = enemy_center_y - center_y

                    distance = np.hypot(tx, ty)

                    if distance < min_dist:
                        min_dist = distance
                        dx, dy = tx, ty - 10  # Adjust y position slightly (as per your code)

        return dx, dy

    def update(self):
        while True:
            if keyboard.is_pressed('o'):
                self.sct.close()  # Close screen capture
                exit(0)

            if keyboard.is_pressed('left alt') or keyboard.is_pressed('right alt'):
                dx, dy = self.get_xy()
                if dx is not None and dy is not None:
                    start = time.perf_counter()
                    self.mouse.move(int(dx * SMOOTH_X), int(dy * SMOOTH_Y))
                    print(f"Tracking target {(time.perf_counter() - start):.4f}")

            if keyboard.is_pressed('v'):
                dx, dy = self.get_xy()
                if dx is not None and dy is not None:
                    start = time.perf_counter()
                    self.mouse.silent_flick(int(dx * 1.4), int(dy * 1.4))
                    print(f"Silent {(time.perf_counter() - start):.4f}")
            else:
                time.sleep(0.01)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--vid', help='Arduino Vendor ID', default=None)
    parser.add_argument('--pid', help='Arduino Product ID', default=None)
    parser.add_argument('--pcode', help='Pingcode from your Arduino Firmware', default=None)

    args = parser.parse_args()

    print(f'{Fore.LIGHTWHITE_EX}Initializing YOLO...', end='')
    game = Game(int(args.vid, 16), int(args.pid, 16), int(args.pcode, 16))
    print(f'\r{Fore.LIGHTWHITE_EX}Initialized         ', end='\n', flush=True)
    print(f'{Fore.LIGHTWHITE_EX}"Alt" - Aimbot')
    print(f'{Fore.LIGHTWHITE_EX} "V"  - Silent Aimbot')
    print(f'{Fore.LIGHTWHITE_EX} "O"  - Exit  ')
    game.update()
