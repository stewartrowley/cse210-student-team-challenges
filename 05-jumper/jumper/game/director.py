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
        
    def start_game(self):

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
    
        guess = self.console.write("Guess a letter [a-z]: ")

        
 
    def do_updates(self):
      

    def do_outputs(self):

        output = self.board.display_word()
        self.console.write(output)


    
