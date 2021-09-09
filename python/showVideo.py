import cv2
import datetime
import cv2
import threading


class RTSPVideoWriterObject(object):
    def __init__(self, src, startTime):
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src)
        # Default resolutions of the frame are obtained (system dependent)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))
        self.fileName = startTime.strftime('%Y-%m-%d %H:%M:%S')
        # Set up codec and output video settings
        self.codec = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        self.output_video = cv2.VideoWriter('{}.avi'.format(str(self.fileName)), self.codec, 30,
                                            (self.frame_width, self.frame_height))

    def show_frame(self):
        # Display frames in main program
        if self.status:
            cv2.imshow('frame', self.capture.read())

        # Press Q on keyboard to stop recording
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            self.output_video.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        frame = self.capture.read()
        # Save obtained frame into video output file
        self.output_video.write(frame)




if __name__ == '__main__':
    url = 'rtsp://admin:admin@192.168.0.2:554'
    currentTime = datetime.datetime.now();
    video_stream_widget = RTSPVideoWriterObject(url, currentTime)
    timer = threading.Timer(5, lambda: video_stream_widget.capture.release)
    timer2 = threading.Timer(7, lambda: exit(1))
    timer.start()
    timer2.start()
    while True:
        video_stream_widget.save_frame()




