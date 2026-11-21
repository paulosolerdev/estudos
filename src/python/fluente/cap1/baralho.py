import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = ["spades", "diamonds", "clubs", "hearts"]

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card("7", "diamonds")
# print(beer_card)

deck = FrenchDeck()
# print(len(deck))

""" deck[0]  # Ace of spades
# print(Card(rank="2", suit="spades"))

deck[-1]  # King of hearts
# print(Card(rank="A", suit="hearts"))

choice(deck)  # Random card
print(Card(rank="3", suit="hearts"))

choice(deck)
print(Card(rank="K", suit="spades"))

choice(deck)
print(Card(rank="2", suit="clubs"))

deck[:3]
print(
    Card(rank="2", suit="spades"),
    Card(rank="3", suit="spades"),
    Card(rank="4", suit="spades"),
)

deck[12::13]
[
    Card(rank="A", suit="spades"),
    Card(rank="A", suit="diamonds"),
    Card(rank="A", suit="clubs"),
    Card(rank="A", suit="hearts"),
]

print("$================================================$")

for card in deck:
    print(card)


print("$================================================$")


for card in reversed(deck):
    print(card)
 """

print(Card("Q", "hearts") in deck)
print(Card("7", "beasts") in deck)
