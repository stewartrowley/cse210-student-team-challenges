import random
class Word_Bank:

    def __init__(self):
        self.word_list = []
        self.word = ""
    def get_word(self):
        number = random.randint(0, 10000)
        text = open(r"wordlist.10000.txt")
        for object in text.readlines():
            self.word_list.append(object)
        self.word = self.word_list[number]
        
        return self.word

