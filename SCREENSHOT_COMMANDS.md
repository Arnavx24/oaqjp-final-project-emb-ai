# Screenshot Generation Commands & Instructions

This document provides the exact commands and visual steps required to produce the required project screenshots for peer review submission.

---

## 1. Screenshot: 6b_deployment_test.png

### Objective
Capture the working web deployment showing a valid emotion detection response.

### Steps
1. **Start the Flask server:**
   ```bash
   python3 server.py
   ```
   *(Ensure terminal shows `Running on http://127.0.0.1:5000`)*

2. **Open your browser and navigate to:**
   ```
   http://localhost:5000/
   ```

3. **Interact with the interface:**
   - Locate the input text area labelled **Text to Analyze**.
   - Type or paste the following sentence:
     ```
     I think I am having fun
     ```
   - Click the blue/submit button labelled **Run Sentiment Analysis**.

4. **Capture the Screenshot:**
   - Wait for the formatted response to appear under the button:
     `For the given statement, the system response is 'anger': 0.003..., 'disgust': 0.001..., 'fear': 0.002..., 'joy': 0.98..., and 'sadness': 0.008... The dominant emotion is joy.`
   - Take a clear screenshot of the entire web interface including:
     - Header ("Emotion Detector")
     - Text box containing `I think I am having fun`
     - "Run Sentiment Analysis" button
     - System response text with emotion scores and dominant emotion `joy`
   - Save the file as:
     `6b_deployment_test.png`

---

## 2. Screenshot: 7c_error_handling_interface.png

### Objective
Capture error handling behavior when blank input is submitted.

### Steps
1. **Ensure the Flask server is running:**
   ```bash
   python3 server.py
   ```

2. **Navigate to (or refresh) the web page:**
   ```
   http://localhost:5000/
   ```

3. **Interact with the interface:**
   - Ensure the input text area is completely blank / empty.
   - Click the button labelled **Run Sentiment Analysis**.

4. **Capture the Screenshot:**
   - Verify the error message displays below the button:
     `Invalid text! Please try again!`
   - Take a clear screenshot showing:
     - Empty text area
     - "Run Sentiment Analysis" button
     - The output message `Invalid text! Please try again!`
   - Save the file as:
     `7c_error_handling_interface.png`
