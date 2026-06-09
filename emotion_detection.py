import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=payload, headers=headers)
    
    try:
        # Convert response text to dictionary
        response_dict = json.loads(response.text)
        
        # Extract emotions and their scores
        emotions = response_dict.get('documentEmotion', {})
        # Filter only the required emotions
        required_emotions = {emotion: emotions.get(emotion, 0) for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
        
        # Find the dominant emotion
        dominant_emotion = max(required_emotions, key=required_emotions.get)
        dominant_score = required_emotions[dominant_emotion]
        
        # Return the desired format
        return {
            "dominant_emotion": dominant_emotion,
            "dominant_score": dominant_score,
            "emotions": required_emotions
        }
        
    except (json.JSONDecodeError, KeyError) as e:
        return {"error": "Failed to parse response or missing fields", "details": str(e)}





"""

def emotion_detector(text_to_analyze):
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        myobj = { "raw_document": { "text": text_to_analyze } }
        response = requests.post(url, json = myobj, headers=header)
        return response.text

"""

