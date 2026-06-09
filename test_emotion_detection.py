from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1["emotions"], 'joy')
        result_1 = emotion_detector("I am really mad about this")
        self.assertEqual(result_1["emotions"], 'anger')
        result_1 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_1["emotions"], 'disgust')
        result_1 = emotion_detector("I am so sad about this")
        self.assertEqual(result_1["emotions"], 'sadness')
        result_1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_1["emotions"], 'fear')


unittest.main()