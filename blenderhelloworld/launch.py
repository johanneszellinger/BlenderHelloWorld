#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# file: launch.py
# Created on : 2024-04-23
# by : Roland Deschain
# 
#
#
# --- imports -----------------------------------------------------------------
import os
import debugpy


# The following lines start a debug server which vscode's debugger can attach to
# the server needs to be started only once (and doesn't stop after running the script. 
# It throws an error if we try to  listen to the same port multiple time, so we solve 
# this simply by wrapping it in a try-except
print("start up debugger. ")
try:
    debugpy.listen(5678)
except RuntimeError as e:
    print("debug server already running. Skipping...")
finally:
    if not debugpy.is_client_connected():
        debugpy.wait_for_client()
print("debugger attached. ")


# The following line executes the actual pyhton script. 
script_path = r"C:\path\to\main.py"

filename = os.path.join(script_path)
exec(compile(open(filename).read(), filename, 'exec'))

