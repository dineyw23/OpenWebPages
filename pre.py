import sys
import webbrowser
from time import sleep

def start():
    with open(sys.argv[1],"r") as f:
        while True:
            line = f.readline()
            if line:
                webbrowser.open(line,new=0,autoraise=True)
                sleep(5)
start()
            