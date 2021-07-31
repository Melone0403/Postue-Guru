import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
shoulder_cascade = cv2.CascadeClassifier('haarcascadeupperbody.xml')

#face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.6
# To capture video from webcam. 

# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
class VideoCamera(object):
    def __init__(self):
       #capturing video
       print("Hello starting the camera")
       self.video = cv2.VideoCapture(0) 
    
    def stop_frame(self):
        #releasing camera
        self.video.release()
    
    
    def get_frame(self):            
    #extracting frames
        success, img = self.video.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        shoulders = shoulder_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw the rectangle around each face
        max_area = 0
        max_face = None
        for (x, y, w, h) in faces:
            if  w*h > max_area:
                max_area = w*h
                max_face = x
        # input key 
        key = True
        choose = True

        # variable holders for keeping 
        x1 = 0
        y1 = 0
        z1 = 0
        w1 = 0

        # adjustment input keys
        a = 20 # adding length
        b = 30 # adding height

        for (x, y, w, h) in faces:
            if x == max_face:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                while key == True:
                    cv2.rectangle(img, (x-a, y-b), (x+w+a, y+h+b), (0, 255,0), 2)
                    if choose == True:
                        key = False
                        x1 = x
                        y1 = y
                        z1 = x+w
                        w1 = y+h
                        break

        cv2.rectangle(img, (x1-a, y1-b), (z1-a, w1-b), (0, 0, 255), 2)

        for (x, y, w, h) in shoulders:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # encode OpenCV raw frame to jpg and displaying it
        # shoulder rectangles
        #cv2.imshow("",img)
        #ret, jpeg = cv2.imencode('.jpg', img)
        return img
VideoCamera().get_frame()