from flask import Flask, render_template, Response, jsonify,request
import cv2
from detect_posture import VideoCamera
app = Flask(__name__)

#camera = VideoCamera()
my_x=0
my_y=0
my_x1=0
my_y1=0
my_ar=0

@app.route('/')
def index():
    print(" I am in root path")
    #return "Hello World"
    return render_template('index.html')


def cali_frames(camera):  
    while True:
        ret, buffer = cv2.imencode('.jpg', camera.cali_frame())
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

def gen_frames(camera):  
    while True:
        ret, buffer = cv2.imencode('.jpg', camera.get_frame())
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/cali_feed')
def cali_feed():
    cam = VideoCamera(0,0,0,0,0,False)
    #print("This is working",req.args)
    res= Response(cali_frames(cam), mimetype='multipart/x-mixed-replace; boundary=frame')
    my_x= cam.static_x
    my_y = cam.static_y
    my_x1= cam.static_x1
    my_y1= cam.static_y1
    my_ar = cam.max_area
    return(res)

@app.route('/cali_res')
def cali_res():
    #print("This is working",req.args)
    cali_res={'x':my_x,'y':my_y,'x1':my_x1,'y1':my_y1,'area':my_ar}
    return Response(jsonify(cali_res))

@app.route('/video_feed')
def video_feed():
    print("This is working",request.args.get('x'))
    return Response(gen_frames(VideoCamera(int(request.args.get('x')),int(request.args.get('y')),\
        int(request.args.get('x1')),int(request.args.get('y1')),int(request.args.get('area')),True)), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port="5000", debug=True)