import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        response = emotion_detector(
            "I am glad this happened"
        )
        self.assertEqual(
            response["dominant_emotion"],
            "joy"
        )

    def test_anger(self):
        response = emotion_detector(
            "I am really mad about this"
        )
        self.assertEqual(
            response["dominant_emotion"],
            "anger"
        )

    def test_disgust(self):
        response = emotion_detector(
            "I feel disgusted"
        )
        self.assertEqual(
            response["dominant_emotion"],
            "disgust"
        )

    def test_fear(self):
        response = emotion_detector(
            "I am afraid"
        )
        self.assertEqual(
            response["dominant_emotion"],
            "fear"
        )

    def test_sadness(self):
        response = emotion_detector(
            "I am very sad"
        )
        self.assertEqual(
            response["dominant_emotion"],
            "sadness"
        )


unittest.main()