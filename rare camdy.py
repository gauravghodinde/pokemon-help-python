
#pip install android-controller
import android_controller
#pip install pure-python-adb
from ppadb.client import Client
#pip install cv2
import cv2


def sceneshot():
    adb = Client(host='127.0.0.1', port=5037)
    devices = adb.devices()

    if len(devices) == 0:
        print('no device attached')
        quit()

    device = devices[0]
    while True:
        image = device.screencap()

        with open('screfgfgen.png', 'wb') as f:
            f.write(image)
        image_1 = cv2.imread(r"C:\Users\Tejas\screfgfgen.png") # your directory adress



sceneshot() # select it and press contol + k + c to disable screenshot action
while True:
    android_controller.tap(1490,630) # (X cordinate , Y coordinate)
    
   
