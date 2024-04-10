from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        new_deck = [0 for _ in range(len(deck))]
        q = deque(range(len(deck)))
        for card in deck:
            index = q.popleft()
            new_deck[index] = card
            if q:
                q.append(q.popleft())
        
        return new_deck
