import os
os.environ['RAYLIB_BIN_PATH'] = r'C:\Users\flipp\cse-210-solo-checkpoints\cse210-student-solo-checkpoints\07-snake\raylib-2.0.0-Win64-mingw\raylib-2.0.0-Win64-mingw\lib'

from game.director import Director
from game.input_service import InputService
from game.output_services import OutputService


def main():
    input_service = InputService()
    output_service = OutputService()
    director = Director(input_service, output_service)
    director.start_game()

if __name__ == "__main__":
    main()
