from pynput import mouse
from pynput import keyboard
from pynput.mouse import Button as button
from pynput.mouse import Controller as mcontroller
from pynput.keyboard import Key as _key
import time

positionA = [0,0]
hasFinishedA = False
positionB = [0,0]
loop = False
started = False

def on_click(x, y, button, pressed):
    global hasFinishedA
    global positionA
    global positionB
    if not pressed:
        if not hasFinishedA:
            positionA[0] = x
            positionA[1] = y
            hasFinishedA = True
        else:
            positionB[0] = x
            positionB[1] = y
        return False

print("Waiting on two positions")
with mouse.Listener(on_click=on_click) as listener:listener.join()
print(positionA)
with mouse.Listener(on_click=on_click) as listener:listener.join()
print(positionB)

_mouse = mcontroller()

def on_press(key):
    global loop
    global started
    loop = True
    if key == _key.backspace:
        return False
    else:
        if started:
            return True
        started = True
        print("started one instance")
        while loop:
            def on_press2(key2):
                global loop
                global started
                if key2 == _key.enter:
                    print("broke loop")
                    loop = False
            listener = keyboard.Listener(on_press=on_press2)
            listener.start()
            _mouse.position = (positionA[0],positionA[1])
            time.sleep(1)
            for x in range(5):
                _mouse.click(button.left, 1)
                time.sleep(0.1)
            _mouse.position = (positionB[0],positionB[1])
            time.sleep(1)
            for x in range(5):
                _mouse.click(button.left, 1)
                time.sleep(0.1)
            time.sleep(1)
            listener.stop()

with keyboard.Listener(on_press=on_press) as listener:listener.join()
print("ended")