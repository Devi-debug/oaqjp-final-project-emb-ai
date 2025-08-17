import requests
import json
def emotion_detector(text_to_analyze):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj={ "raw_document": { "text": text_to_analyze } }
    response=requests.post(url,headers=headers,json=myobj)
    formatted_response=json.loads(response.text)
    emotions=formatted_response['emotionPredictions'][0]['emotion']
    for emotion,score in emotions.items():
        dominant_emotion=max(emotions, key=emotions.get)
        return {"anger":score,"disgust":score,"fear":score,
        "joy":score,"sadness":score,"dominant_emotion":dominant_emotion}

        