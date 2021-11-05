from time import sleep

import raylibpy
from game import constants
from game.word import Word
from game.score_board import ScoreBoard
from game.buffer import Buffer


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
        self._buffer = Buffer()
        self._letters = ""
        self._words_to_remove = []
        
        
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
        self._buffer.get_text(self._letters)
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a word match and updating the score.

        Args:
            self (Director): An instance of Director.
            generate new words
            move words 
            remove words
        """
        
        self._handle_word_match()
        self._generate_new_words()
        self._move_words()
        self._remove_words()
        
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        
        self._output_service.draw_actors(self._word._word_list)
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actor(self._score_board)
        self._output_service.flush_buffer()

    def _handle_word_match(self):
        
        for word in self._word._word_list:
            if self._letters == word:
                self._words_to_remove.append(word)
                points = self._word.get_points(word)
                self._score_board.add_points(points)       

    def _generate_new_words(self):
        self._word._generate_word()

    def _move_words(self):
        self._word.move_word()

    def _remove_words(self):
        for word in self._words_to_remove:
            self._word.reset(word)
