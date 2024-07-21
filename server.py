from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/emotionDetection")
def detect_emotion():
    input_text = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(input_text)


    response_text = (
        f"For the given statemen, the system response is 'anger'. {emotion_result['anger']}",
        f"'disgust'. {emotion_result['disgust']}, 'fear': {emotion_result['fear']}",
        f"'joy'. {emotion_result['joy']} and 'sadness': {emotion_result['sadness']}"
        f"The dominant emotion is {emotion_result['dominant_emotion']}"
    )

    return jsonify({"response": response_text, "result": emotion_result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
