# MIT License

# Copyright (c) 2022 Antoine Marzin

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Portablify script

usage :
    python3 ./portablify.py <app name as configured in json file>

example :
    python3 ./portablify.py signal

    portablify_conf.json :
        {
            "signal":
            {
                "default_app_dir":"/mnt/c/Users/tlda/AppData/Local/Programs/signal-desktop/",
                "portable_app_dir":"/mnt/c/Users/tlda/Apps/Signal/"
            },

            "notion":
            {
                "default_app_dir":"/mnt/c/Users/tlda/AppData/Local/Programs/Notion/",
                "portable_app_dir":"/mnt/c/Users/tlda/Apps/Notion/"
            }
        }


This script was first written to make Electron apps like Signal or Notion portable.

They can be used as portable app, but any updates fired from the app UI
will be installed in the default folder (~/AppData/Local/Programs/).

Running the app through this script will :
 - sync any version in the default folder with the target "portable dir"
   using Rsync
 - remove the default folder
 - run the app from it
"""

import json
import os
import shutil
import subprocess
import sys

# Argument check
if len(sys.argv) > 2:
    print("Too much arguments")
    exit(1)

if len(sys.argv) < 1:
    print("Argument missing, please specify an app name known in the config file")
    exit(1)

# Get argument passed in command line
arg = str(sys.argv[1]).lower()
script_dir = os.path.abspath( os.path.dirname( __file__ ) )

# Load configuration from file
with open(f"{script_dir}/portablify_conf.json", "r") as f:
    conf = json.load(f)

# 
# Run process if app specified in arg is known by config file
#
for a in conf["apps"]:
    if arg == str(a).lower():
        src_dir = conf["apps"][a]['src_dir']
        des_dir = conf["apps"][a]['des_dir']
        exe = conf["apps"][a]['exe']

        try:
            for f in os.listdir(src_dir):
                shutil.move(f"{src_dir}/{f}", des_dir)

        except FileNotFoundError:
            pass

        # Run the app
        subprocess.run(f"{des_dir}/{exe}",
                       stdout=subprocess.DEVNULL)
        # os.system(f"{exe} > /dev/null &") # Posix OSes
        quit(0)

else:
    print(f"{arg} unknown in configuration file")
    exit(1)