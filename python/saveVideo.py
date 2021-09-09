import cv2
import datetime
import os


def writeVideo():
    currentTime = datetime.datetime.now()
    cap = cv2.VideoCapture('rtsp://admin:admin@192.168.0.2:554')
    # 웹캠 설정
    cap.set(3, 960)  # 영상 가로길이 설정
    cap.set(4, 480)  # 영상 세로길이 설정
    fps = 20
    width = int(cap.get(3))  # 가로 길이 가져오기
    height = int(cap.get(4))  # 세로 길이 가져오기
    fileName = str(currentTime.strftime('%Y %m %d %H %M %S'))

    path = f'D:/Github_cctv/myhomeCCTV/python/{fileName}.avi'
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')  # DIVX 코덱 적용 # 코덱 종류 # DIVX, XVID, MJPG, X264, WMV1, WMV2
    out = cv2.VideoWriter(path, fcc, fps, (width, height))
    # 비디오 저장을 위한 객체를 생성한다# cv2.VideoWriter(저장 위치, 코덱, 프레임, (가로, 세로))
    while True:
        ret, frame = cap.read()
        cv2.imshow('divx', frame)  # 촬영되는 영상보여준다.
        out.write(frame)  # 촬영되는 영상을 저장하는 객체에 써준다.
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    cap.release()  # cap 객체 해제
    out.release()  # out 객체 해제
    cv2.destroyAllWindows()


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


writeVideo()
