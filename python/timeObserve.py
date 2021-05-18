from threading import Thread
import time
import datetime
from datetime import timedelta
from concurrent.futures import ThreadPoolExecutor
import shutil

def hello_world():
    sleep(1)
    return "hello world"

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread", total)
class TimeDifferCheck():
    def __init__(self):
        self.settingTime = datetime.datetime.now()
        self._return = None
    
    def checkCurrentTime(self):
        currentTime = datetime.datetime.now()
        print("CurrentTime : ",currentTime.strftime('%Y-%m-%d %H %M %S'))
        time.sleep(0.5)

    def checkTimeForSecond(self):
        print("Start")
        while True:
            currentTime = datetime.datetime.now()
            differTime = currentTime - self.settingTime
            if int(differTime.seconds) == 5:
                print("Done : ",datetime.datetime.now().strftime('%Y-%m-%d %H %M %S'))
                self.settingTime = datetime.datetime.now()
                return True
            else:
                print("CurrentTime : ",currentTime.strftime('%Y-%m-%d %H %M %S'))
                print("SettingTime : ",self.settingTime.strftime('%Y-%m-%d %H %M %S'))
                
            time(0.5)
    def fileMove(self):
        print("Move start")
        filename = '테넷 (정식자막) TENET.2020.1080p.KOR.FHDRip.H264.AAC-RTM.mkv'
        src = "D:/Tenet/"
        dir = "F:/Test/"
        shutil.move(src+filename,dir+filename)


    def printSecond(self):
        i = 0
        while True:
            
            i +=1
            time(0.5)
            print("Im working : " ,i)
    def join(self):
        Thread.join(self)
        return self._return
        


if __name__ == '__main__':

    
    # print("Main Thread")
    
    pool = ThreadPoolExecutor(1)
    # pool_excutor_Repeat = ThreadPoolExecutor(1)
    
    
    # pool_repeat = pool_excutor_Repeat.submit(timeDifferCheck.printSecond)
    while True:
        timeDifferCheck = TimeDifferCheck()
        t_end = time.time() + 60*3
        fileMove = True
        pool_start = pool.submit(timeDifferCheck.fileMove)
        while time.time() <t_end:
            timeDifferCheck.checkCurrentTime()
            if pool_start.done() and fileMove:
                fileMove = False
                print("MOVE IS DONE")
                

        # result = timeDifferCheck.checkTimeForSecond()
        # print(result)
        # pool = pool_executor_Time.submit(timeDifferCheck.checkTimeForSecond)
        # while not pool.done():

        
        # print("HI")
        # if pool.done():
        #     print("END, But Never Ending")
        

    # pool.
        # sleep(0.5)
    # pool_excutor_Repeat.shutdown()
    
    

    # currentTime = datetime.datetime.now()
    # print(currentTime+1)
    #---------------------------------------------------------
    # timeThread = Thread(target = timeDifferCheck.checkTimeForSecond)
    # repeatThread = Thread(target = timeDifferCheck.printSecond)
    # timeThread.start()
    # repeatThread.start()
    # timeThread.join()
    # repeatThread.join()
    
        
    # while timeThread.is_alive():
        
