#!/usr/bin/env python3

import sys
import argparse
import re

CARDNAME_REGEX = re.compile(r"(\d+ )?([^(]+) ?.*")

class Card():
    def __init__(self, quantity, name):
        self.quantity = quantity
        self.name = name

def parse_quantity(text):
    quantity = text.strip()
    if quantity.endswith("x"):
        quantity = quantity[:-1]
    return int(quantity)

def parse_decklist(text):
    lines = text.splitlines()
    cards = []
    for line in lines:
        if not line:
            continue
        match = CARDNAME_REGEX.search(line)
        if not match:
            print('ERROR: Failed to parse "%s"' % line)
            continue
        if match.lastindex == 2:
            quantity = parse_quantity(match.group(1))
        else:
            quantity = 1

        card_name = match.group(match.lastindex)
        cards.append(Card(quantity, card_name))

    return cards

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("decklist")
    args = parser.parse_args(argv[1:])

if __name__ == "__main__":
    sys.exit(main(sys.argv))
