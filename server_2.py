from flask import Flask, request, render_template, url_for
from EmotionDetection.emotion_detection import emotion_detector
import requests
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detection():
    text = request.args.get("textToAnalyze")
    output = emotion_detector(text)
    
    if output["dominant_emotion"] == None:
        return " Invalid text! Please try again!."
    else:
        return f"""For the given statement, the system response is 
                'anger':{ output['anger']}, 
                'disgust': {output['disgust']}, 
                'fear':{output["fear"]}, 
                'joy': {output["joy"]}, 
                'sadness': {output["sadness"]}, 
                'dominant_emotion': {output["dominant_emotion"]}."""
   
   
@app.route("/")
def render_index_page():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True) 
    app.run(host = "0.0.0.0", port = 5000)  
    
