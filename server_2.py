"""
Emotion Detection Web Application
This module provides a Flask web application for detecting emotions in text.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route("/emotionDetector")
def emotion_detection():
    """ Analyze the emotion in the provided text."""
    text = request.args.get("textToAnalyze")
    output = emotion_detector(text)
    if output["dominant_emotion"] is None:
        return " Invalid text! Please try again!."
    return f"""For the given statement, the system response is
                'anger':{ output['anger']},
                'disgust': {output['disgust']},
                'fear':{output["fear"]},
                'joy': {output["joy"]},
                'sadness': {output["sadness"]},
                'dominant_emotion': {output["dominant_emotion"]}."""
@app.route("/")
def render_index_page():
    """ Render the main index page of the application."""
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
