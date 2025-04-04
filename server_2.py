from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/emotionDetector")

def emotion_detection():
    response = request.args.get("textToAnalyze")
   
    if response.status_code == 200:
        if response["dominant_emotion"] == None:
            return "Invalid text! Please try again!."
        else:
            return f"""The system output is: 'anger':{ response['anger']}, 
                'disgust': {response['disgust']}, 
                'fear':{response["fear"]}, 
                'joy': {response["joy"]}, 
                'sadness': {response["sadness"]}, 
                'dominant_emotion': {response["dominant_emotion"]}."""
    elif response.status_code == 400:
        return f"""The system output is: 'anger':{ None}, 
                'disgust': {None}, 
                'fear':{None}, 
                'joy': {None}, 
                'sadness': {None}, 
                'dominant_emotion': {None}."""
    
    else:
        return "Invalid input! please try again"

@app.route("/")
def render_index_page():
    return reneder_template("index.html")
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
