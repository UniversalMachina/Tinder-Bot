

import time
import keyboard

key_pressed = False

def on_key(event):
    global key_pressed
    key_pressed = True

keyboard.on_press(on_key)
import pyautogui
def swipe_right():
    import random

    def generate_number():
        rand_float = random.random()  # Generate a random float between 0 and 1

        if rand_float <= 0.02:  # 33% chance
            return 2
        else:  # 67% chance
            return 1

    number = generate_number()
    print(number)
    screen_width, screen_height = pyautogui.size()
    start_x = screen_width // 2 -200
    end_x = (screen_width // 2) * 3
    middle_y = screen_height // 2
    middle_x = (screen_width // 2)+100
    if number == 1:
        pyautogui.moveTo(middle_x, middle_y)
        pyautogui.dragTo(end_x, middle_y, duration=0.5, button='left')
    if number == 2:
        pyautogui.moveTo(middle_x, middle_y)
        pyautogui.dragTo(start_x, middle_y, duration=0.5, button='left')


def do_something():
    global key_pressed
    print("Starting the inner loop...")
    counter = 0
    while not key_pressed:
        print("Doing something...")
        swipe_right()
        counter += 1
        print(counter)
        if counter == 200:
            break
        # time.sleep(0.5)  # Add a delay to avoid overwhelming the CPU
    print("Inner loop stopped.")

print("Press any key to stop the loop.")

while not key_pressed:
    do_something()


print("Key pressed. Outer loop stopped.")