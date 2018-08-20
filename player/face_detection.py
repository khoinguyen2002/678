from threading import Thread
import cv2
class Webcam:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.currentFrame = self.cap.read()
        self.getpos = (0,0)
        self.classHar = cv2.CascadeClassifier('nhac/haar.xml')
    def getImagefromCam(self):
        while True:
            ret,self.currentFrame = self.cap.read()
            self.currentFrame = cv2.flip(self.currentFrame,1)
            #ret, Img = self.cap.read()
            #ret, frame = self.cap.read()
            #Himage = frame.shape[0]  # lay ve so rows cua anh?
            # convert rgb to gray
            gray = cv2.cvtColor(self.currentFrame, cv2.COLOR_RGB2GRAY)
            faces = self.classHar.detectMultiScale(gray)
            x_facemax = 0
            y_facemax = 0
            w_facemax = 0
            h_facemax = 0
            for x, y, w, h in faces:
                if w * h > w_facemax * h_facemax:
                    x_facemax = x
                    y_facemax = y
                    w_facemax = w
                    h_facemax = h
            cv2.rectangle(self.currentFrame, (x_facemax, y_facemax), (x_facemax + w_facemax, y_facemax + h_facemax), (0, 0, 225), 5)
            # cv2.imshow("video original", Img)
            self.getpos = (x_facemax + w_facemax/2,y_facemax + h_facemax/2)
            cv2.namedWindow("Videowebcam");
            cv2.moveWindow("Videowebcam", 800, 0);
            cv2.imshow('Videowebcam',self.currentFrame)
            key = cv2.waitKey(1)
            if (key&0xFF == ord('q')):
                break
    def update(self):
        Thread(None,self.getImagefromCam).start()



