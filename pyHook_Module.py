
from pynput.keyboard import Key, Controller
import pyautogui, time

testList = ["w", "t8", "w", "0" "wt", "t8", "w", "u0", "w", "y7", "w", "q", "wt", "y7", "w", "uq", "w", "t8", "w", "0", "wt", "u8"]
interstellar = ["u", "t", "u", "t", "u", "t", "u", "t", "u", "t", "u","t","u", "t", "u", "t", "u", "t", "u", "t", "u", "t", "u","t","60eu","t","u","t","u","t","7ru","y","u","y","u","y","u","y","u","60eu","t","7ru","y","8wtu","y","7ru","y","60eu","t","7ru","y","8twu","y","u","y","u","y","7ru","y","u","y","u","48qeup","uf"," ","eup","uf"," ","59wrua"]
noteListTest = ["aP", "Yui", "TOP"]
maro =["9u","9u"," ","9u"," ","9t","9u"," ","wo"," ",'5w'," ","tw",]

start_time = time.time()
seconds = 0
starttime = time.time()
bpm = 1

time.sleep(5 - ((time.time() - starttime) % 5))
for x in maro:
    pyautogui.write(x)
    pyautogui.press("enter")
    time.sleep(bpm - ((time.time() - starttime) % bpm))
current_time = time.time()
elapsed_time = current_time - start_time
print("Finished iterating in: " + str(int(elapsed_time)) +" seconds.")



