#!/usr/bin/env python3

import sys
import argparse
import re
import json
import sqlite3

CARDNAME_REGEX = re.compile(r"(\d+ )?([^(]+) ?.*")
CARD_BACK_URL = "TBD cardback URL"

REQUEST_URL = "https://api.scryfall.com/cards/named?exact=%s"

class CardDatabase():
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        # TODO(phil): Create table and cache Scryfall queries.

    def close()
        self.connection.close()

    def get(self, card_name):
        if

class Card():
    def __init__(self, quantity, name):
        self.quantity = quantity
        self.name = name

    def get_url(self):
        return "TBD cardfront URL"

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

def generate_tts_file(cards):
    tts = dict(ObjectStates=[])
    tts["ObjectStates"].append({
        "ContainedObjects": [{
            "CardId": (i + 1) * 100,
            "Name": "Card",
            "Nickname": card.name,
            "Transform": {
                "posX": 0,
                "posY": 0,
                "posZ": 0,
                "rotX": 0,
                "rotY": 180,
                "rotZ": 180,
                "scaleX": 1,
                "scaleY": 1,
                "scaleZ": 1
            },
        } for i, card in enumerate(cards)],
        "CustomDeck": {
            str(i + 1): {
                "BackIsHidden": True,
                "BackURL": CARD_BACK_URL,
                "FaceURL": card.get_url(),
                "NumHeight": 1,
                "NumWidth": 1
            } for i, card in enumerate(cards)
        },
        "DeckIDs": [
            (i + 1) * 100 for i, card in enumerate(cards) for q in range(card.quantity)
        ],
        "Name": "DeckCustom",
        "Transform": {
            "posX": 0,
            "posY": 1,
            "posZ": 0,
            "rotX": 0,
            "rotY": 180,
            "rotZ": 180,
            "scaleX": 1,
            "scaleY": 1,
            "scaleZ": 1
        },
    })
    return tts

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("decklist")
    args = parser.parse_args(argv[1:])

    with open(args.decklist) as file:
        decklist = file.read()
    cards = parse_decklist(decklist)
    tts = generate_tts_file(cards)

    print(json.dumps(tts, indent=4, sort_keys=True))

if __name__ == "__main__":
    sys.exit(main(sys.argv))
