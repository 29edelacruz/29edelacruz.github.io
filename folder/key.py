import time
import keyboard

DELAY = 0.060

_stop_flag = False
def _stop():
    global _stop_flag
    _stop_flag = True

keyboard.add_hotkey('f6', _stop) # press F6 to stop
print("Press F6 to stop. Starting auto key presser...")

try:
    while not _stop_flag:
        keyboard.send('f5')
        time.sleep(DELAY)
except KeyboardInterrupt:
    pass

print("Stopped")