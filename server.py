"""
Emotion Detector Flask Application
"""

from flask import Flask
from flask import request

from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze emotion route.
    """

    text_to_analyze = request.args.get(
        "textToAnalyze"
    )

    response = emotion_detector(
        text_to_analyze
    )

    if response["dominant_emotion"] is None:
        return (
            "Invalid text! "
            "Please try again!"
        )

    return (
        f"For the given statement, "
        f"the system response is {response}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render home page.
    """

    return (
        "Emotion Detector Running"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )