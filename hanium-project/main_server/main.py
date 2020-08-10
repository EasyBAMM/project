from flask import Flask, render_template, redirect, url_for 

app = Flask(__name__) 

# sample
url_server = {
                "water" : "http://192.168.35.66:5000",
                "trafficlight1" : "http://192.168.35.39/5000",
                "trafficlight2" : "http://192.168.35.39/5000",
                "waterhose" : "http://192.168.35.267/5000",
                "car1" : "http://192.168.35.8:5000",
                "car2" : "http://192.168.35.26:5000",
                "car1_camera" : "http://192.168.35.8:5000/video_feed",
                "car2_camera" : "http://192.168.35.26:5000/video_feed",
                "robotarm" : "http://192.168.35.34/5000",                
            }

@app.route('/')
@app.route('/index')  
def home():
    
    return render_template('index.html')

    
@app.route('/cctv') 
def cctv():

    return render_template('cctv.html', url_server=url_server)

@app.route('/data') 
def data():

    return render_template('data.html')

@app.route('/control') 
def control():

    return render_template('control.html')    

@app.route('/frame') 
def frame():

    return render_template('frame.html', url_server=url_server, enumerate=enumerate) 


if __name__ == '__main__':
    app.run(debug=True)
