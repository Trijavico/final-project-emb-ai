"""
server.py: A Flask application for emotion detection.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Serve the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetection")
def detect_emotion():
    """
    Handle POST requests to detect emotions from text.
    
    Returns a JSON response with emotion scores and the dominant emotion.
    """
    input_text = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(input_text)

    if emotion_result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again."}), 400

    return jsonify(emotion_result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
