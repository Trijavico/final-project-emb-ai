import requests, json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url= URL, json= input, headers= Headers)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = response.json()

    emotion_scores = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disguts', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0)
    }

    dominant = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant

    return emotion_scores
