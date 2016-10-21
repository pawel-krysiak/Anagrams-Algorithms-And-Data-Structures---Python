import unittest
from anagrams import Anagrams

class TestAnagrams(unittest.TestCase):

    def setUp(self):
        self.anagrams = Anagrams()

    def tearDown(self):
        self.anagrams = None

    def test_first_run(self):
        self.assertEqual(self.anagrams.find_anagrams('open'), [])

    def test_finding_nope(self):
        self.assertEqual(self.anagrams.find_anagrams('open'), [])
        self.assertEqual(self.anagrams.find_anagrams('nope'), ['open'])

    def test_not_returning_duplicates(self):
        self.assertEqual(self.anagrams.find_anagrams('open'), [])
        self.assertEqual(self.anagrams.find_anagrams('open'), ['open'])
        self.assertEqual(self.anagrams.find_anagrams('open'), ['open'])
        self.assertEqual(self.anagrams.find_anagrams('nope'), ['open'])

    def test_finding_words_with_zero_length(self):
        self.assertEqual(self.anagrams.find_anagrams(''), [])
        self.assertEqual(self.anagrams.find_anagrams(''), [])

    def test_finding_words_with_one_char_length(self):
        self.assertEqual(self.anagrams.find_anagrams('a'), [])
        self.assertEqual(self.anagrams.find_anagrams('a'), ['a'])

    def test_not_returning_words_with_different_lenght(self):
        self.assertEqual(self.anagrams.find_anagrams('a'), [])
        self.assertEqual(self.anagrams.find_anagrams('aa'), [])
        self.assertEqual(self.anagrams.find_anagrams('a'), ['a'])

    def test_different_character_cases(self):
        self.assertEqual(self.anagrams.find_anagrams('open'), [])
        self.assertEqual(self.anagrams.find_anagrams('Nope'), ['open'])

if __name__ == '__main__':
    unittest.main()
