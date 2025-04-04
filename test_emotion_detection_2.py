from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        tests = {"joy": "I am glad this happened",
        "anger":"I am really mad about this",
        "disgust":"I feel disgusted just hearing about this",
        "sadness":"I am so sad about this",
        "fear":"I am really afraid that this will happen"
        }
        results = {}
        for k,v in tests.items():
            result = emotion_detector(v)
            results[result["dominant_emotion"]] = k 
        output = list(results.keys())
        true_output =  list(results.values())
        self.assertEqual(output, true_output)

unittest.main()


