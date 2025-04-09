import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        texts = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for text, emotion in texts.items():
            result = emotion_detector(text)
            self.assertEqual(result["dominant_emotion"], emotion)


if __name__ == "__main__":
    unittest.main()
