"Flask-based AI application for emotion detection"

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector as emotion_detection

app = Flask(__name__)


@app.route("/")
def home():
    """Home template handler function"""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector():
    """Route handler for GET /emotionDetector"""
    text = request.args.get("textToAnalyze")

    result = emotion_detection(text)
    print(result)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )
    return response_str


if __name__ == "__main__":
    app.run(debug=True, port=5000)
