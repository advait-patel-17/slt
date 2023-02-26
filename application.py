from flask import Flask, render_template, Response, jsonify
import cv2
from turbo_flask import Turbo
from HandTracker import getletter

app = Flask(__name__)
turbo = Turbo(app)

camera = cv2.VideoCapture(0)

message = ""
def gen_frames():  # generate frame by frame from camera
    global message
    counter = 0
    character = '?'
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            frame, letter = getletter(camera, success, frame)
            if (letter != character):
                character = letter
                counter = 1
            elif (counter == 20):
                message += letter
                print(message)
                counter = 0
            else:
                counter += 1
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html', message = message)

@app.route('/update')
def update():
    # Increment the variable by 1
    # global my_variable
    # my_variable += 1
    global message
    # message = message + "h"
    # Update the variable on the page using TurboFlask
    print("message " + message)
    return jsonify(message)

    # Return an empty response
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)