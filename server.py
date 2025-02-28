'''Application analyzes supplied text and assesses emotional information from the data.'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Application")

@app.route("/emotionDetector")
def detect_emotion():
    '''Method analyzes the text supplied and returns back the results to the page.'''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {anger_score}, \
        'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and \
        'sadness': {sadness_score}. The dominant emotion is <b>{dominant_emotion}<b>"

@app.route("/")
def render_home_page():
    '''Method renders the home page for the application.'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
