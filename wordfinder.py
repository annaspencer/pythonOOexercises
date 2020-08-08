"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self, path):
        """ sets file by path, reads file, returns # of lines read"""
        file = open(path)
        self.word_list = self.parse(file)
        print(f"{len(self.word_list)} words read")

    def parse(self, file):
        """takes away whitespace in each line"""
        return [w.strip() for w in file]

    def random(self):
        """picks a random line"""

        return random.choice(self.word_list)

class SpecialWordFinder(WordFinder):
    
    def parse(self, file):
        """same parse function, but skips blank lines and lines that 
        start with #"""
        return [w.strip() for w in file
            if w.strip() and not w.startswith("#")]