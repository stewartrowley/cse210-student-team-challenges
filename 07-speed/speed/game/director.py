from time import sleep

import raylibpy
from game import constants
from game.word import Word
from game.score_board import ScoreBoard


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        word (Word): The users target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score_board = ScoreBoard()
        self._letters = ""
        
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self._output_service.open_window("Speed")

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print("Game over!")

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        self._letters = self._input_service.get_letter()
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a word match and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        
        self._handle_word_match()
        
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        
        self._output_service.draw_actors(self._word_list)
        self._output_service.draw_text(10, 10, self._letters, True)
        self._output_service.draw_actor(self._score_board)
        self._output_service.flush_buffer()

    def _handle_word_match(self):
        if self._letters == self._word:
            points = self._word.get_points()
            self._score_board.add_points(points)
            self._word_reset()