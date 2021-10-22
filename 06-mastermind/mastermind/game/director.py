from game.board import Board
from game.console import Console
from game.guess import Guess
from game.player import Player
from game.roster import Roster

class Director:

    def __init__(self):
       
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._guess = Guess(self._board.code)
        self._roster = Roster()
        
        
    def start_game(self):
        
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
    
    def _get_inputs(self):
        player = self._roster.get_current()
        board = self._board.to_string(self._roster)
        self._console.write(board)
    
        
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number("What is your guess ")
        player.set_guess(guess)

    def _do_updates(self):
        
        player = self._roster.get_current()
        guess = player.get_guess()
        hint = self._guess.make_hint(guess)
        self._board.apply(guess, hint)
 
    def _do_outputs(self):
        
        if self._board.did_win():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()

     
       