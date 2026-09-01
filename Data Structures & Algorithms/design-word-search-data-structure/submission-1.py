class Node:
    def __init__(self, value):
        self.value = value
        self.isWordEnd = False
        self.nextChars = dict()
class WordDictionary:
    # in the case of the dot, how can I continue the search efficiently?
    # store keys seen at each layer?
    #   d b m
    #  a |a |e
    #   |  |y

    # can't find prefixes has to be full words 
    # end chars have to have isWordEnd field 
    # how would i be able to with a ., determine which next char in the trie to traverse to to guarantee a correct answer?? 
    # ami thinking too much abt this?
    def __init__(self):
        self.trie = Node("")
        

    def addWord(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie.nextChars:
                trie.nextChars[c] = Node(c)
            trie = trie.nextChars[c]
        trie.isWordEnd = True
        

    def search(self, word: str) -> bool:
        t = self.trie
        possibleTries = [t]
        for c in word:
            nextPossibleTries = []
            for trie in possibleTries:
                if c == ".":
                    for nextTrie in trie.nextChars.values():
                        nextPossibleTries.append(nextTrie)
                else:
                    if c in trie.nextChars:
                        nextTrie = trie.nextChars[c]
                        nextPossibleTries.append(nextTrie)
            if len(nextPossibleTries) == 0:
                return False
            possibleTries = nextPossibleTries
        
        for lastTrie in possibleTries:
            if lastTrie.isWordEnd:
                return True
        return False

        

