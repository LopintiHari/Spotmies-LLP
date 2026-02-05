from trie import Trie

trie = Trie()

words = ["car", "care", "cat", "carbon", "cart", "car", "cat", "car"]
for word in words:
    trie.insert(word)

print(trie.get_suggestions("c", 5))
print(trie.get_suggestions("car", 3))
print(trie.get_suggestions("z", 2))
