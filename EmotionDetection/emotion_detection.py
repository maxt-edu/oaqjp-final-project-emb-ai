__all__ = ["emotion_detector"]
import requests as req


def emotion_detector(text_to_analyze: str):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    response = req.post(
        url,
        json={"raw_document": {"text": text_to_analyze}},
        headers={
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        },
    )
    result = response.json()
    scores = result["emotionPredictions"][0]["emotion"]
    scores["dominant_emotion"] = max(scores, key=scores.get)
    return scores
