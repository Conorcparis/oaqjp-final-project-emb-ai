import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": f"Request failed with status code {response.status_code}"}

    result = json.loads(response.text)
    
    emotion_scores = result['emotionPredictions'][0]['emotion']
    
    # Extract the required emotions
    anger = emotion_scores.get('anger', 0)
    disgust = emotion_scores.get('disgust', 0)
    fear = emotion_scores.get('fear', 0)
    joy = emotion_scores.get('joy', 0)
    sadness = emotion_scores.get('sadness', 0)

    # Find the dominant emotion
    emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    
    dominant_emotion = max(emotions, key=emotions.get)

    # Return the formatted result
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
