# Spotmies-LLP
# Trie Data Structure for Text autocomplete.

## About the project
This project implements a Trie (prefix tree) data structure in Python.
The main goal is to support fast word insertion, searching, and
autocomplete suggestions based on prefixes.

The Trie is built using a sample corpus of words, and suggestions are ranked using simple frequency counts.

## Major Implementations
1. Inserting words into the Trie
2. Searching whether a word exists
3. Get autocomplete suggestions for a given prefix
4. Return top-k suggestions based on frequency
5. Case-insensitive handling of words
6. Unit tests using pytest

## How to run
1. Run the tests using:
    python -m pytest

2. (Optional) To run manual Testing
    python -m main

## Time Complexity
i. Inserting a word takes O(L), where L is the length of the word.
ii. Searching for a word also takes O(L).
iii. Autocomplete suggestions take O(P + N log N), where:
        a. P is the prefix length
        b. N is the number of matching words

## Space Complexity
i. The Trie uses O(total characters) across all inserted words.
ii. Common prefixes are shared, which helps reduce memory usage.

## Testing
Unit tests are written using 'pytest' to check:
    i.Word insertion
    ii. Word search
    iii. Prefix-based suggestions
    iv. Frequency-based ordering
    v. Case-insensitive behavior


## This task really helped me understand how Tries are used in real autocomplete systems.