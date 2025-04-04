from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/emotionDetector")


def emotion_detection():

    response = request.args.get["textToAnalyze"]
    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score  = response["fear"]
    joy_score  = response["joy"]
    sadness_score  = response["sadness"]
    dominant_detector  = response["dominant_emotion"]
    
    if dominant_detector == None:
        return "Invalid text! Please try again!."
    else:
        return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_detector}."


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)