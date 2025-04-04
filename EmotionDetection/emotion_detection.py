import requests
import json
def emotion_detector(text_to_analyse):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)
    
    out = json.loads(response.text)
    print("output is ", out)
    highest_score = 0
    dominant_emotion=""
    if response.status_code == 400:
        output = {'anger': None, 'disgust': None, 'fear': None, 'joy': None,
         'sadness': None, 'dominant_emotion': None }
    else:
        for emotion, score in out["emotionPredictions"][0]["emotion"].items():
            if score > highest_score:
                highest_score= score
                dominant_emotion = emotion
        output = out["emotionPredictions"][0]["emotion"]
        output.update({'dominant_emotion': dominant_emotion})
   

    return output






# from emotion_detection import emotion_detector;emotion_detector("love")