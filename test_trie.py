from trie import Trie

def test_trie():
    trie = Trie()
    words = ["car", "care", "cat", "car", "cat", "car"]

    for word in words:
        trie.insert(word)

    assert trie.search("car") is True
    assert trie.search("care") is True
    assert trie.search("dog") is False

    suggestions = trie.get_suggestions("ca", 2)
    assert suggestions == ["car", "cat"]

def test_case_insensitive():
    trie = Trie()
    trie.insert("Car")
    trie.insert("CAR")
    trie.insert("car")

    assert trie.search("car") is True
    assert trie.total_words() == 1
    assert trie.get_suggestions("CA", 1)[0] == "car"

def test_empty_prefix():
    trie = Trie()
    trie.insert("hello")
    trie.insert("help")
    assert trie.get_suggestions("he", 2) == ["hello", "help"]


