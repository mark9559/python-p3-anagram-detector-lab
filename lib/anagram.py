# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        matches = []
        sorted_word = sorted(self.word)
        
        for candidate in candidates:
            lower_candidate = candidate.lower()
            if lower_candidate != self.word and sorted(lower_candidate) == sorted_word:
                matches.append(candidate)
        
        return matches
