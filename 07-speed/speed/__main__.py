import os
os.environ['RAYLIB_BIN_PATH'] = r'C:\Users\StewM\Documents\BYU Idaho\Fall 2021\programmingCourses\CSE210_personal\cse210-student-solo-checkpoints-1\07-snake\libraylib_shared.dll'

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
