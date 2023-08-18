class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        """
        first make curr = root
        iterate through all characters in word
        if char not present in children of root, make new Nde
        else current = current.children[character]
        finally make last char == end of word
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
        

    def search(self, word):
        """
        start from root node
        iterate through every char in word
        check if it matches with children
        if NOT return false
        if TRUE keep repeating until reached last char
        if last char is end of word - return True
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord

        

    def startsWith(self, prefix):
        """
        in this case we will just check if atleast one word contains prefix
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True



