#!/usr/bin/env python3

import unittest

from ttsmtg import CARDNAME_REGEX, parse_decklist

class TestClass(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_regex(self):
        match = CARDNAME_REGEX.search("1 Card name, and comma (SET)")
        self.assertTrue(match)
        self.assertEqual(match.lastindex, 2)
        self.assertEqual(match.group(1), "1 ")
        self.assertEqual(match.group(2), "Card name, and comma ")

    def test_decklist(self):
        with open("testdata.txt", "r") as file:
            decklist = file.read()
        cards = parse_decklist(decklist)
        # We have 80 unique cards and 100 cards in total.
        self.assertEqual(80, len(cards))
        self.assertEqual(100, sum([card.quantity for card in cards]))


if __name__ == "__main__":
    unittest.main()
