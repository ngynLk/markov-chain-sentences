# Simple Markov Chain Sentence Generator written in Python

> What is it?

A Markov chain is a chain where the next phase of it can't be predicted using the former phases. This is what is used in this little program to create sentences starting from a word.

A text is passed to it and used as a base to choose the words from. Starting from the word given it will choose between the different words that are located right after in the text.

> How does it work? 

It is written in the form of a Python class `MarkovClass` with four methods `find_next`, `_find_ender`, `make_sentence` and `make_text` (`_find_ender` is used to find words that are at the end of sentences to have more sensible results)

A simple CLI front-end may be written afterwards

