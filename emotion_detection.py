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
    response = requests.post(url, json=myobj, headers-header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    return formatted_response