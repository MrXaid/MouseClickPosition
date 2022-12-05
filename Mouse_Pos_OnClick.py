from pynput import mouse
import pyautogui


mouse_ = mouse.Controller()
button = mouse.Button


# Click detection function
def on_click(x, y, button, pressed):
    btn = button.name

    # Left Click detection, You can also change it to Right if you want to get the mouse position on Right Click
    if btn == 'left':
        if pressed:
            try:
                # Method to get the Current Mouse Cursor Postion
                
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr)

            except KeyboardInterrupt:
                print('\nDone')


with mouse.Listener(
        on_click=on_click
) as listener:
    listener.join()



