import requests
import json

def emotion_detector(text_to_analyze):
    # URL for Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Payload for Emotion Predict API
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Headers for Emotion Predict API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # POST request and capture response
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    response_json = json.loads(response.text)

    # If the response status code is 200, extract the emotion scores and dominant emotion
    if response.status_code == 200:
        # Get required emotions and scores dictionary
        scores = response_json['emotionPredictions'][0]['emotion']
        
        # Extract the dominant emotion
        dominant_emotion = list(scores.keys())[list(scores.values()).index(max(scores.values()))]
        
        # Format the response
        formatted_response = { key:scores[key] for key in scores}
        formatted_response['dominant_emotion'] = dominant_emotion
    
    # If the response status code is 400, set all response values to None
    elif response.status_code == 400:
        formatted_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    return formatted_response
