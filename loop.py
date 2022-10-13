import svg_extrude
import os
import shutil

FRAMES = 3286
origin = r'STLs\frame0183_black.stl'

for i in range(FRAMES):
    target = r'STLs\frame%04d_black.stl' % (i+1)
    if(not os.path.exists(target)):
        print(i+1)
        shutil.copyfile(origin, target)
