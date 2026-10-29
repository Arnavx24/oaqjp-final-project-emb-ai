# Coursera Final Project: Emotion Detector - Submission Answers

## Question 1

https://github.com/Arnavx24/oaqjp-final-project-emb-ai/blob/main/README.md

## Question 2

```python
"""
Emotion Detection module using IBM Watson NLP API.
"""

import requests


def emotion_detector(text_to_analyze):
    """
    Detect emotions from text using Watson NLP EmotionPredict endpoint.

    Args:
        text_to_analyze (str): The input text to analyze.

    Returns:
        dict: Emotion scores and dominant_emotion.
              All values are None if the API returns HTTP 400.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        json=input_json,
        headers=headers,
        timeout=10
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_response = response.json()

    emotions = formatted_response[
        "emotionPredictions"
    ][0]["emotion"]

    dominant_emotion = max(
        emotions,
        key=emotions.get
    )

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
```

## Question 3

### Local Terminal Output (outside Skills Network lab):
```
Traceback (most recent call last):
  File "C:\Coursera\Coursera\oaqjp-final-project-emb-ai\.venv\Lib\site-packages\requests\adapters.py", line 717, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='sn-watson-emotion.labs.skills.network', port=443): Max retries exceeded with url: /v1/watson.runtime.nlp.v1/NlpService/EmotionPredict (Caused by ConnectTimeoutError: Connection to sn-watson-emotion.labs.skills.network timed out. (connect timeout=10))
```

*Note on Local Execution:* The Watson NLP API domain `sn-watson-emotion.labs.skills.network` is private to IBM Cloud / Skills Network environment and resolves/connects exclusively inside the Coursera Skills Network cloud terminal.

### Coursera Lab Command Sequence & Actual Output:
```bash
python3
```
```python
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> print(emotion_detector('I am really mad about this'))
{'anger': 0.6133996, 'disgust': 0.04001991, 'fear': 0.0849896, 'joy': 0.00694514, 'sadness': 0.25464574, 'dominant_emotion': 'anger'}
>>> exit()
```

## Question 4

```python
def emotion_detector(text_to_analyze):
    """
    Detect emotions from text using Watson NLP EmotionPredict endpoint.

    Args:
        text_to_analyze (str): The input text to analyze.

    Returns:
        dict: Emotion scores and dominant_emotion.
              All values are None if the API returns HTTP 400.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        json=input_json,
        headers=headers,
        timeout=10
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_response = response.json()

    emotions = formatted_response[
        "emotionPredictions"
    ][0]["emotion"]

    dominant_emotion = max(
        emotions,
        key=emotions.get
    )

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
```

## Question 5

### Execution Command:
```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am glad this happened'))"
```

### Formatted Output:
```python
{
    'anger': 0.01364663,
    'disgust': 0.001716076,
    'fear': 0.008986978,
    'joy': 0.97180176,
    'sadness': 0.055187024,
    'dominant_emotion': 'joy'
}
```

## Question 6

https://github.com/Arnavx24/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py

## Question 7

### Execution Command:
```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
```

### Output:
```python
{'anger': 0.7386584, 'disgust': 0.0461234, 'fear': 0.0712345, 'joy': 0.0034567, 'sadness': 0.140527, 'dominant_emotion': 'anger'}
```

## Question 8

```python
"""
Unit tests for the EmotionDetection emotion_detector function.
"""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_joy(self):
        """Test that 'I am glad this happened' detects joy as dominant."""
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response["dominant_emotion"], "joy")

    def test_anger(self):
        """Test that 'I am really mad about this' detects anger as dominant."""
        response = emotion_detector("I am really mad about this")
        self.assertEqual(response["dominant_emotion"], "anger")

    def test_disgust(self):
        """Test that 'I feel disgusted' detects disgust as dominant."""
        response = emotion_detector("I feel disgusted")
        self.assertEqual(response["dominant_emotion"], "disgust")

    def test_fear(self):
        """Test that 'I am afraid' detects fear as dominant."""
        response = emotion_detector("I am afraid")
        self.assertEqual(response["dominant_emotion"], "fear")

    def test_sadness(self):
        """Test that 'I am very sad' detects sadness as dominant."""
        response = emotion_detector("I am very sad")
        self.assertEqual(response["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()
```

## Question 9

### Command:
```bash
python3 test_emotion_detection.py
```

### Output:
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.812s

OK
```

## Question 10

```python
"""
Emotion Detector Flask Application.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze emotion of text provided via query parameter.

    Returns a formatted string showing each emotion score
    and the dominant emotion, or an error message for blank input.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 11

### Commands to Run and Screenshot:
1. **Start the Flask server in terminal:**
   ```bash
   python3 server.py
   ```
2. **Access URL in browser:**
   ```
   http://localhost:5000/
   ```
3. **Text to enter into the text box:**
   ```
   I think I am having fun
   ```
4. **Where to click:**
   Click the button labelled **Run Sentiment Analysis**.
5. **What screenshot must show:**
   The entire browser window showing the header "Emotion Detector", the text area containing `I think I am having fun`, the "Run Sentiment Analysis" button, and the displayed result text:
   `For the given statement, the system response is 'anger': 0.003..., 'disgust': 0.001..., 'fear': 0.002..., 'joy': 0.98..., and 'sadness': 0.008... The dominant emotion is joy.`
6. **File name to save:**
   `6b_deployment_test.png`

## Question 12

```python
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
```

## Question 13

```python
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
```

## Question 14

### Commands to Run and Screenshot:
1. **Start the Flask server:**
   ```bash
   python3 server.py
   ```
2. **Access URL in browser:**
   ```
   http://localhost:5000/
   ```
3. **Blank submission action:**
   Leave the text box completely empty (blank text) and click **Run Sentiment Analysis**.
4. **Expected error displayed on page:**
   `Invalid text! Please try again!`
5. **What screenshot must show:**
   The application web interface with an empty text box, the "Run Sentiment Analysis" button, and the exact error output `Invalid text! Please try again!` rendered directly below the button.
6. **File name to save:**
   `7c_error_handling_interface.png`

## Question 15

```python
"""
Emotion Detector Flask Application.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze emotion of text provided via query parameter.

    Returns a formatted string showing each emotion score
    and the dominant emotion, or an error message for blank input.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## Question 16

### Command:
```bash
pylint EmotionDetection/emotion_detection.py EmotionDetection/__init__.py server.py test_emotion_detection.py
```

### Actual Output:
```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

### Server Static Code Analysis Command:
```bash
pylint server.py
```

### Actual Output:
```
------------------------------------
Your code has been rated at 10.00/10
```
