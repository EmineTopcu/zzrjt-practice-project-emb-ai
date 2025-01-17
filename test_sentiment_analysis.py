import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyser

class TestSentimentAnalyser(unittest.TestCase):
    def test_sentiment_analyser(self):
        result1 = sentiment_analyser('I love working with Python')
        self.assertEqual(result1['label'], 'SENT_POSITIVE')

        result2 = sentiment_analyser('I hate working with Python')
        self.assertEqual(result2['label'], 'SENT_NEGATIVE')
        
        result3 = sentiment_analyser('I am neutral with Python')
        self.assertEqual(result3['label'], 'SENT_NEUTRAL')
        
unittest.main()