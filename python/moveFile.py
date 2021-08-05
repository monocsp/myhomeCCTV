import shutil
import os

filename = 'tenet'
fileFormat = '.mkv'
src = "F:/tenet/"
destination = "E:/tenet/"


def moveFile():
    try:
        isCurrentPathFileExist = os.path.isfile(src + filename + fileFormat)
        isDestinationFileExist = os.path.isfile(destination + filename + fileFormat)
        if isCurrentPathFileExist:
            if not isDestinationFileExist:
                shutil.move(src + filename + fileFormat, destination + filename + fileFormat)
            else:
                i = 1
                while True:
                    if os.path.isfile(destination + filename + " ({})".format(i) + fileFormat):
                        i += 1
                    else:
                        break
                shutil.move(src + filename + fileFormat, destination + filename + " ({})".format(i) + fileFormat)
        else:
            print("File No Exist")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("Start")
    moveFile()
    print("End")
