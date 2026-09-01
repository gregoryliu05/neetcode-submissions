class Node:
    def __init__(self, value = "", isWordEnd = False):
        self.value = value
        self.isWordEnd= isWordEnd
        self.nextValues = dict()
class PrefixTree:
    # how can i determine word vs just a prefix?
    # if we instert word and then call startsWith(word) imma assume false.

    # 1. dictionary of words
    # 2. or a node class with isWordEnd field

    # key-value pairs 

    # value, nextChars, isWordEnd



    def __init__(self):
        self.trie = Node()
        

    def insert(self, word: str) -> None:
        trie = self.trie
        for i, c in enumerate(word):
            if c not in trie.nextValues:
                trie.nextValues[c] = Node(c)
            trie = trie.nextValues[c]
        trie.isWordEnd = True


    def search(self, word: str) -> bool:
        trie = self.trie
        for i, c in enumerate(word):
            if c not in trie.nextValues:
                return False
            trie = trie.nextValues[c]
        return trie.isWordEnd
        

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for i, c in enumerate(prefix):
            if c not in trie.nextValues:
                return False
            trie = trie.nextValues[c]
        return True
        
        