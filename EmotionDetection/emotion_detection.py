import requests
import json
def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    
    formatted_response = json.loads(response)
    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score  = None
        joy_score  = None
        sadness_score  = None
        dominant_detector= None
    else:
        anger_score = formatted_response["anger"]
        disgust_score = formatted_response["disgust"]
        fear_score  = formatted_response["fear"]
        joy_score  = formatted_response["joy"]
        sadness_score  = formatted_response["sadness"]

        best_score = 0
        for k,v in formatted_response.items():
            if v >  best_score:
                best_score = v
                dominant_detector = k

    return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_detector
            }