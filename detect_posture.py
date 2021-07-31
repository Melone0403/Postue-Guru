import cv2
import notifyUser as nf
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
shoulder_cascade = cv2.CascadeClassifier('haarcascadeupperbody.xml')

# To capture video from webcam. 
#cap = cv2.VideoCapture(0)
# To use a video file as input 
#cap = cv2.VideoCapture('filename.mp4')

# ----- REPLACE IMAGE SJDHKFSDFKJ--------
waitframe = 100 

class VideoCamera(object):
    def __init__(self,x,y,x1,y1,max_ar,cali):
       #capturing video
       print("Hello starting the camera")
       self.video = cv2.VideoCapture(0) 
       self.static_x = x
       self.static_y = y
       self.static_x1 = x1
       self.static_y1 = y1
       self.old_frame = cali
       self.max_area=max_ar
   
    def stop_frame(self):
        #releasing camera
        self.video.release()
    
    def cali_frame(self):      
        success,static_img = self.video.read()
        #cv2.imshow("win",static_img)
        print("It is workimg",self.old_frame)
        if self.old_frame == False :
            print("Checking for one frsme")
            static_gray = cv2.cvtColor(static_img, cv2.COLOR_BGR2GRAY)

            static_faces = face_cascade.detectMultiScale(static_gray, 1.1, 4)

            # find max face
            self.max_area = 0
            max_face = None
            for (x, y, w, h) in static_faces:
                if  w*h > self.max_area:
                    self.max_area = w*h
                    max_face = x

            self.static_x = 0
            self.static_y = 0
            self.static_x1 = 0
            self.static_y1 = 0
            img = None

            for (x, y, w, h) in static_faces:
                if max_face == x:
                    self.static_x = x
                    self.static_y = y
                    self.static_x1 = x+w
                    self.static_y1 = y+h
                    img = cv2.rectangle(static_img, (x, y), (x+w, y+h), (0, 0, 255), 2)

            print("Let me see if this works")
            old_frame = True
            print(self.max_area,self.static_x,self.static_y,self.static_x1,self.static_y1)
                    # cv2.rectangle(img, (x-a, y-b), (x+w+a, y+h+b), (0, 255,0), 2)
                    
                    #cv2.imshow("Video", static_img)
        return static_img

    def get_frame(self):      
        success,static_img = self.video.read()
        #cv2.imshow("win",static_img)
        print("It is workimg")
        if self.old_frame==True:
            print("OLD FRAME TAKEN")
            # Read the frame
            #success, img = cap.read()
            img = static_img
            #cv2.imshow("win",img)
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect the faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            shoulders = shoulder_cascade.detectMultiScale(gray, 1.3, 5)
            print("Good Job")
            # Draw the rectangle around each face
            self.max_area = 0
            max_face = None
            for (x, y, w, h) in faces:
                if  w*h > self.max_area:
                    self.max_area = w*h
                    max_face = x
            
            # input key 
            key = True
            choose = 0
            
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
                    # cv2.rectangle(img, (x-a, y-b), (x+w+a, y+h+b), (0, 255,0), 2)
                    
                    
            img = cv2.rectangle(img, (self.static_x, self.static_y), (self.static_x1, self.static_y1), (0, 0, 255), 2)
            
            # detect bad posture (x1, ...)-> bad posture
            for (x, y, w, h) in faces:
                if x == max_face:
                    # if (x1-a > x) and (x > x1+a) and (y1-b < y) and (y < y1+b):
                    print(self.static_y,y)
                    if (self.static_y+50 < y):
                        print ("erro")
                        nf.show_mess()      
                
            for (x, y, w, h) in shoulders:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                       
            # shoulder rectangles
            static_img= img    
        return static_img
        # All done, release device
