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
