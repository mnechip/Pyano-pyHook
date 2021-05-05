
from pynput.keyboard import Key, Controller
import pyautogui, time

testList = ["aTD7xdh7LP", "Ku03m6He2X", "LVI9m421RE", "O4cKyQwqP4"]

start_time = time.time()
seconds = 0
starttime = time.time()
bpm = 5

for x in testList:
    pyautogui.write(x)
    pyautogui.press("enter")
    time.sleep(bpm - ((time.time() - starttime) % bpm))
current_time = time.time()
elapsed_time = current_time - start_time
print("Finished iterating in: " + str(int(elapsed_time)) +" seconds.")



