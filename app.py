from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS,cross_origin
from src.ccnClassifier.utils.common import decodeImage
from src.ccnClassifier.pipeline.prediction import Predictionpipeline

os.putenv("LANG","en_us.UTF-8")
os.putenv("LC_ALL","en_US.UTF-8")

app= Flask(__name__)
CORS(app)

class Clientapp:
    def __init__(self):
        self.filename="inputimage.jpg"
        self.classifeir=Predictionpipeline(self.filename)

@app.route("/",methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train",methods=["GET","POST"])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    #os.system("dvc repro")

    return "training done sucessfully"



@app.route("/predict",methods=["GET","POST"])
@cross_origin()
def predictRoute():   
    image=request.json["image"]
    decodeImage(image,clapp.filename)
    result= clapp.classifeir.predict()
    return jsonify(result)

if __name__=="__main__":
    clapp=Clientapp()

    app.run(host="0.0.0.0",port=8080) #for coolify
