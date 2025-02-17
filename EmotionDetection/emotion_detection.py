import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_body = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=json_body)
    response_dict = dict()
    response_dict.update({"dominant_emotion" : None})
    if response.status_code != "200":
        response_dict.update({"anger" : None})
        response_dict.update({"disgust" : None})
        response_dict.update({"fear" : None})
        response_dict.update({"joy" : None})
        response_dict.update({"sadness" : None})
        return response_dict

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion_score = 0.000
    for emotion in emotions:
        emotion_score = emotions[emotion]
        response_dict.update({emotion : emotion_score})
        if dominant_emotion_score < emotion_score:
            response_dict.update({"dominant_emotion" : emotion})
            dominant_emotion_score = emotion_score
    return response_dict