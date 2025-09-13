import sys
import os
import platform

colors = True  # Output should be colored
machine = sys.platform  # Detecting the os of current system
checkplatform = platform.platform() # Get current version of OS
if machine.lower().startswith(('os', 'darwin', 'ios')):
    colors = False  # Colors shouldn't be displayed on mac & windows
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    colors = True
    os.system('')   # Enables the ANSI
if not colors:
    reset = red = white = green = yellow = run = bad = good = info = what = back = reset = orange = gray = ''
else:
    gray = '\033[90m'
    green = '\033[92m'
    blue = '\033[34m'
    red = '\033[91m'
    yellow = '\033[93m'
    orange = '\033[38;5;208m'
    back = '\033[7;91m'
    info = '\033[93m[!]'
    what = '\033[94m[?]'
    thing = '\033[90m[-]'
    notgood = '\033[91m[X]' # >:3c
    good = '\033[92m[+]'
    run = '\033[97m[~]'
    correct = '\033[34m[✔]'
    reset = '\033[37m'