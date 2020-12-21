import re
import random


class MarkovChain:
    def __init__(self, filepath):
        """ contructor, takes the filepath to a text that is used as dictionnary to create sentences """
        # open file at filepath and create array self.dictionnary from it
        with open(filepath, 'r') as file:
            text = file.read()
            # only keep alphabetic characters, spaces and dots
            text = re.sub(r'[^0-9À-ÿa-zA-Z\'\-\. ]+', '', text)
            text = re.sub(r' *\. *$', '. ', text)
            text = re.sub(r'\.', '. ', text)
            self.dictionnary = text.split(' ')
            # clean dictionnary by removing empty items and single dots
            while True:
                try:
                    self.dictionnary.pop(self.dictionnary.index(r''))
                except ValueError:
                    break
            while True:
                try:
                    self.dictionnary.pop(self.dictionnary.index(r'.'))
                except ValueError:
                    break
        random.seed()

    def make_sentence(self, word, length):
        """ returns a string with the sentence created with the Markov chain (self.find_next), based on the parameter `word` """
        # lowercase the word and remove dot if there is
        word = re.sub(r'\.*$', '', word)
        # initialize array sentence with the first word
        sentence = [word]
        # add words to sentence
        for i in range(length):
            word = random.choice(self.find_next(word))
            sentence.append(word)
        # capitalize the first word and adding an ender
        sentence[0] = sentence[0][0].upper() + sentence[0][1:]
        sentence.append(self._find_ender(sentence))
        # return a string
        return ' '.join(sentence)

    def make_text(self, length):
        """ returns multiple sentences created with `make_sentence` that start with a random word """
        text = []
        for i in range(length):
            text.append(self.make_sentence(random.choice(
                self.dictionnary), random.randint(15, 20)))
            if random.random() < 0.25:
                text.append('\n')
        return ''.join(text)

    def find_next(self, word):
        """ returns list of words than can come next based on word passed as argument """
        possibilities = []
        # loop through the whole dictionnary to find the word passed as argument
        for i in range(len(self.dictionnary)):
            # handling exceptions if IndexError
            try:
                if self.dictionnary[i] == word and not self._is_ender(self.dictionnary[i+1]):
                    # add the next word from the dictionnary to the possibilities (excludes the enders that end with a dot)
                    possibilities.append(self.dictionnary[i+1])
            except IndexError:
                continue
        # if there are no possibilities add a random word
        if len(possibilities) == 0:
            possibilities.append(random.choice(self.dictionnary))
        return possibilities

    def _find_ender(self, sentence):
        """ returns one of the words that close a sentence (words that end with a dot) """
        possibilities = []
        for i in self.dictionnary:
            try:
                if self._is_ender(i):
                    possibilities.append(
                        '{} '.format(i))
            except IndexError:
                pass
        # return a single dot if there isn't anything
        if len(possibilities) == 0:
            possibilities.append(random.choice(self.dictionnary) + '. ')
        # check if the ender of the sentence can be one of the predictions (otherwise return a random one.)
        return_values = []
        for i in possibilities:
            if i in self.find_next(sentence[-1]):
                return_values.append(i)
        if len(return_values) == 0:
            return_values.append(random.choice(possibilities))
        return random.choice(return_values)

    def _is_ender(self, word):
        return word[-1] == '.'


if __name__ == '__main__':
    chain = MarkovChain('/home/me/text')
    print(chain.make_text(20))
