import unittest
from data.preprocess_text import preprocess_text

class TestPreprocessText(unittest.TestCase):
    def test_preprocess_text(self):
        text = "This is a sample text for testing."
        expected_result = "This is a sample text for testing"
        self.assertEqual(preprocess_text(text), expected_result)

if __name__ == '__main__':
    unittest.main()