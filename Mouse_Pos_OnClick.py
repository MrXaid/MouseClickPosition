from pynput import mouse
import pyautogui


mouse_ = mouse.Controller()
button = mouse.Button

def on_click(x, y, button, pressed):
    btn = button.name

    if btn == 'left':
        if pressed:
            # mouse_.click(button.left)
            # print('works')
            try:
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr)

            except KeyboardInterrupt:
                print('\nDone')


with mouse.Listener(
        on_click=on_click
) as listener:
    listener.join()


# Second Code starts from here



#try:
#    while True:
#        x, y = pyautogui.position()
#        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#        print(positionStr)

#except KeyboardInterrupt:
#    print('\nDone')


