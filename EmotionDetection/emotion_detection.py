import requests
import json



"""

def emotion_detector(text_to_analyze):
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        myobj = { "raw_document": { "text": text_to_analyze } }
        response = requests.post(url, json = myobj, headers=header)
        
        return response.text



print(emotion_detector("Hate"))

"""



def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=payload, headers=headers)
    
    try:
        response_dict = json.loads(response.text)
        
        # Extract emotions from the first item in emotionPredictions
        emotions = response_dict['emotionPredictions'][0]['emotion']
        
        dominant_emotion = max(emotions, key=emotions.get)
        dominant_score = emotions[dominant_emotion]
        
        return {
            "dominant_emotion": dominant_emotion,
            "dominant_score": dominant_score,
            "emotions": emotions
        }
        
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        return {"error": "Failed to parse response or missing fields", "details": str(e)}

#print(emotion_detector("Hate"))