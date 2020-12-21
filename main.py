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
            text = re.sub(r'\.+', '. ', text)
            self.dictionnary = text.split(' ')
            while True:
                try:
                    self.dictionnary.pop(self.dictionnary.index(''))
                except ValueError:
                    break
        random.seed()

    def make_sentence(self, word, length):
        """ returns a string with the sentence created with the Markov chain (self.find_next), based on the parameter `word` """
        # lowercase the word and remove dot if there is
        word = re.sub(r'\.+$', '', word)
        # initialize array sentence with the first word
        sentence = [word]
        # add words to sentence
        for i in range(length):
            word = self.find_next(word)
            sentence.append(word)
        # capitalize the first word and adding an ender
        try:
            sentence[0] = sentence[0][0].upper() + sentence[0][1:]
        except IndexError:
            print(sentence)
        sentence.append(self.find_ender())
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
        """ returns next word based on word passed as argument """
        possibilities = []
        # loop through the whole dictionnary to find the word passed as argument
        for i in range(len(self.dictionnary)):
            # handling exceptions if IndexError
            try:
                if self.dictionnary[i] == word and re.match('\.$', self.dictionnary[i+1]) == None:
                    # add the next word from the dictionnary to the possibilities (excludes the enders that end with a dot)
                    possibilities.append(self.dictionnary[i+1])
            except IndexError:
                continue
        # if there are no possibilities add a random word
        if len(possibilities) == 0:
            possibilities.append(random.choice(self.dictionnary))
        # return one of the possibilities
        return random.choice(possibilities)

    def find_ender(self):
        """ returns one of the words that close a sentence (words that end with a dot) """
        possibilities = []
        for i in self.dictionnary:
            try:
                if i[-1] == '.':
                    possibilities.append(i + ' ')
            except IndexError:
                continue
        # return a single dot if there isn't anything
        if len(possibilities) == 0:
            possibilities.append('.')
        return random.choice(possibilities)


if __name__ == '__main__':
    chain = MarkovChain('/home/me/text')
    print(chain.make_text(20))
