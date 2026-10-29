# Final Commands Reference

Sequential list of all terminal commands used in the Emotion Detector project for execution, testing, code quality checks, and deployment.

---

## 1. Environment Setup & Dependency Verification
```bash
# Activate virtual environment (if using local venv)
source .venv/bin/activate    # Linux / macOS / Coursera Terminal
# .venv\Scripts\Activate.ps1 # Windows PowerShell

# Install required packages
pip install requests flask pylint
```

---

## 2. Package & Function Verification (Tasks 2 & 3)
```bash
# Test emotion_detector directly in Python shell
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))"

# Test formatted output package import
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
```

---

## 3. Unit Testing (Tasks 4 & 5)
```bash
# Run the 5 unit test cases (joy, anger, disgust, fear, sadness)
python3 test_emotion_detection.py
```

---

## 4. Static Code Analysis - Pylint (Tasks 7 & 8)
```bash
# Run pylint across all modules
pylint EmotionDetection/emotion_detection.py EmotionDetection/__init__.py server.py test_emotion_detection.py

# Run pylint specifically on the Flask server
pylint server.py
```

---

## 5. Web Application Deployment (Task 6)
```bash
# Start Flask server on port 5000
python3 server.py

# In browser:
# Open http://localhost:5000/
# Test valid sentence: "I think I am having fun" -> Save screenshot as 6b_deployment_test.png
# Test blank sentence: "" -> Save screenshot as 7c_error_handling_interface.png
```

---

## 6. Git Version Control & Submission
```bash
# Check status of modified and added files
git status

# Stage all files
git add .

# Commit project changes
git commit -m "Complete Emotion Detector project: Watson NLP API, Flask server, unit tests, pylint 10/10"

# Push to your GitHub fork
git push origin main
```
