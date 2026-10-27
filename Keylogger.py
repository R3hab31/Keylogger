from pynput import keyboard as keys
from datetime import datetime as dt
from tracker import key_press  
log_file = "keylog.txt"
listener=None
pressed=set()
def init_log():
    with open(log_file,"w") as w:
        start=dt.now().strftime( "%d-%m-%Y %H:%M:%S")
        w.write(f"===session start : {start} ===\n\n") 

def write(text):
    timestamp=dt.now().strftime( "%d-%m-%Y %H:%M:%S")
    with open(log_file,"a") as w:
        w.write(f"[{timestamp}] {text} \n")

def on_press(key):
    global pressed
    if key in pressed:
        return
    pressed.add(key)
    try:
        k=key.char
        write(f"Pressed: {k}")
        key_press(k)
    except AttributeError:
        write(f"Special: {key}")
        key_press(str(key))

def on_release(key):
    global pressed
    if key in pressed:
        pressed.remove(key)
    if key==keys.Key.esc:
        write("=== Session Ended ===")
        return False
    
def start_log():
    global listener
    if listener and listener.is_alive():
        return listener
    init_log()
    listener=keys.Listener(on_press=on_press,
                           on_release=on_release)
    listener.daemon=True
    listener.start()
    return listener 

def clear_log():
    with open(log_file,"w") as w:
        start = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        w.write(f"===session start : {start}===\n\n")   