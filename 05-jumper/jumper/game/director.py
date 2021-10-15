from game.console import Console
from game.jumper import Jumper
from game.board import Board
from game.word_bank import Word_Bank

class Director:

    def __init__(self):
        
        self.console = Console()
        self.jumper = Jumper()
        self.board = Board()
        self.word_bank = Word_Bank()
        self.keep_playing = True
        self.guess = ""
        
    def start_game(self):

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
    
        self.guess = self.console.read("Guess a letter [a-z]: ")

 
    def do_updates(self):

        word = self.word_bank.get_word()
        self.jumper.check_guess(word)


    def do_outputs(self):

        output = self.board.display_word(self.guess)
        self.console.write(output)
        self.console.write(self.board.display_jumper(self.jumper.wrong))
        self.keep_playing = (self.jumper.wrong != 5)


    
