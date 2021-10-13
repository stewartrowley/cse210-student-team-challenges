from game.console import Console
from game.jumper import Jumper


class Director:

    def __init__(self):
        
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        
    def start_game(self):

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
    
        message = self.jumper.get_message()
        self.console.write(message)
        
    def do_updates(self):
      
    
        
    def do_outputs(self):
    
