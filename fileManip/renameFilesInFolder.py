# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os


baseFolder = "E:\\tv\\[HR] Ben 10 - Alien Force S01-03 COMPLETE [Web 1080p x265]~HR-GZ"
fileList = os.listdir(baseFolder)

for file in fileList:
    # Sets the complete path for the source filename
    src = baseFolder + "\\" + file

    # Sets the base path for the destination filename
    dst = baseFolder + "\\"

    # adds modified filename to the base path, to make complete path for destination filename.
    dst += file.split()[-1]

    # renames files
    os.rename(src, dst)
    print(dst)

# for count, filename in enumerate(os.listdir(baseFolder)):
#     dst = "Hostel" + str(count) + ".jpg"
#     src = 'xyz' + filename
#     dst = 'xyz' + dst
#
#     os.rename(src, dst)
