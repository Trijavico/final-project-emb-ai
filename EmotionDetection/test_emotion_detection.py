import unittest
from emotion_detection import emotion_detector

class EmotionDetectionTest(unittest.TestCase):

    def test_emotion_detector(self):
        test_cases = [
            ('I am glad this happened', 'joy'),
            ('I am really mad about this', 'anger'),
            ('I feel disgusted just hearing about this', 'disgust'),
            ('I am so sad about this', 'sadness'),
            ('I am really afraid that this will happen' 'fear')
        ]

        for statement, dominant in test_cases:
            result = emotion_detector(statement)
            self.assertEqual(result['dominant_emotion'], dominant)

if __name__ == "__main__":
    unittest.main()
