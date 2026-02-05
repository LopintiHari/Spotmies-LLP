class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0   # For tracking unique words

    def insert(self, word):
        word = word.lower() # For case sensitive issues
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        if not node.is_end:
            self.word_count +=1
        node.is_end = True
        node.frequency += 1

    def search(self, word):
        word = word.lower() # For case sensitive issues
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def _collect_words(self, node, prefix, result):
        if node.is_end:
            result.append((prefix, node.frequency))
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, result)

    def get_suggestions(self, prefix, k):
        prefix = prefix.lower()
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        result = []
        self._collect_words(node, prefix, result)
        result.sort(key=lambda x: x[1], reverse=True)
        return [word for word, freq in result[:k]]
    
    def starts_with(self, prefix):
        prefix = prefix.lower()
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def total_words(self):
        return self.word_count
