import sys
import os

def bp():
    current_path = os.path.dirname(__file__)
    egg_loc = os.path.join(current_path, "pycharm-debug.egg")
    sys.path.append(egg_loc)
    #print egg_loc
    import pydevd
    pydevd.settrace("localhost", port=12345, stdoutToServer=True, stderrToServer=True)
