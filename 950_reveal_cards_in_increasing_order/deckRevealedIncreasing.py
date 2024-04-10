class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = []
        for x in sorted(deck)[::-1]:
            d = [x] + d[-1:] + d[:-1]
        return d