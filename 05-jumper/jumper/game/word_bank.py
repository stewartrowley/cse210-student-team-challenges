import random
class Word_Bank:

    def __init__(self):
        self.word_list = []
        self.word = ""
    def get_word(self):
        number = random.randint(0, 10000)
        text = open("05-jumper\jumper\game\wordlist.10000.txt", "r")
        object = text.readlines()
        items = []
        for i in object:
            items.append(i)

        self.word_list = [x[:-1]for x in items]


        self.word = self.word_list[number]
        
        return self.word

