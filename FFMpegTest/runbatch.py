import os
import subprocess
import time

start = time.time()

srcDir = os.path.abspath("wav")
toDir = os.path.abspath("result")
fileExt = (".wav")

try:
    os.makedirs(toDir)
except:
    pass
for root, dirs, files in os.walk(srcDir, topdown=True):
    for file in files:
        src = os.path.join(root, file)
        filename, ext = os.path.splitext(file)
        target = os.path.join(toDir, file)
        if file.lower().endswith(fileExt):
            index = 1
            while os.path.exists(target):
                index +=1
                target = os.path.join(toDir, os.path.splitext(file)[0]+ "_%d" % index + ext)
            print("Converting: '%s'  to  '%s'" % (src, target.replace(".wav",".mp3")))
            cmd = "ffmpeg -i " + src + " -vn -c:a libmp3lame -qscale:a 1 -ac 1 " + target.replace(".wav",".mp3")
            p = subprocess.Popen(cmd, stderr=subprocess.PIPE, universal_newlines=True)
print("Moving " + srcDir + " to Recycle Bin")
rec = "recycle.bat " + srcDir
r = subprocess.Popen(rec, stderr=subprocess.PIPE, universal_newlines=True)

end = time.time()
print("Whole operation took " + str(end - start) + " seconds")