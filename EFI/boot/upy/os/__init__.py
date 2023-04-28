# Replace built-in os module.
from uos import *

# Provide optional dependencies (which may be installed separately).
try:
    from . import path
except ImportError:
    pass

##def remove(path):
##    system('del "'+path+'" > NUL')
##
##def rename(path,name):
##    system('rename "'+path+'" "'+name+'" > NUL')
##    #print('rename "'+path+'" "'+name+'" > NUL')
##
###listdir= ilistdir
##def listdir(path="."):
##    return [x[0] for x in ilistdir(path)][2:]

