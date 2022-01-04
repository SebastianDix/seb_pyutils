##setx.py
from __future__ import print_function
import sys, linecache
from pathlib import Path
from color import COLORS as c
import threading

##adapted from https://stackoverflow.com/a/33449763/2454357
##emulates bash's set -x and set +x

##for turning tracing on and off
TRACING = False
IGNORE_SITE_PACKAGES = True

def start_tracing():
    global TRACING
    TRACING=True

##FILENAMES defines which files should be traced
##by default this will on only be the host file 
FILENAMES = [sys.argv[0]]

##flag to ignore FILENAMES and alwas trace all files
##off by default
FOLLOWALL = False

def traceit(frame, event, arg):
    ##from https://stackoverflow.com/a/40945851/2454357
    # while frame.f_code.co_filename.startswith('<frozen'):
    #     frame = frame.f_back
    filename = frame.f_code.co_filename
    lineno = frame.f_lineno
    line = linecache.getline(filename, lineno)
    if "tolkien" in line:
    # print("{}, {} {}".format(c.bold_green(Path(filename).name), lineno, line.rstrip()))
        print("{}, {} {}".format(c.bold_green(Path(filename)), lineno, line.rstrip()))
    # return traceit

# def my_tracer(frame, event, arg = None):
#     filename = frame.f_code.co_filename
#     if IGNORE_SITE_PACKAGES:
#         if 'site-packages' in Path(filename).parts:
#             return
#         if 'lib' in Path(filename).parts:
#             return
#         if filename[0] == "<":
#             return
#     # extracts frame code
#     code = frame.f_code
#     # extracts calling function name
#     func_name = code.co_name
#     # extracts the line number
#     line_no = frame.f_lineno
#     print(f"A {event} encountered in \
#     {func_name}() at line number {line_no} ")
#     return my_tracer

sys.settrace(traceit)
sys.setprofile(traceit)
threading.settrace(traceit)
