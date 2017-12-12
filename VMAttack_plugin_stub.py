# coding=utf-8
__author__ = 'Anatoli Kalysch'

import imp
import sys
import os

DEBUG = True

F_DIR = os.environ["VMAttack"]
F_NAME = "VMAttack.py"
sys.path.append(F_DIR)

plugin_path = os.path.join(F_DIR, F_NAME)
if DEBUG:
    print "Debug in VMAttack_plugin_stub.py"
    print "[VMAttack_plugin_stub.py] plugin_path:" + plugin_path
    print "[VMAttack_plugin_stub.py] __name__:" + __name__
plugin = imp.load_source(__name__, plugin_path)
PLUGIN_ENTRY = plugin.PLUGIN_ENTRY