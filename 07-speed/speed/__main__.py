from game.output_services import OutputService
from game.input_service import InputService
import os
os.environ['RAYLIB_BIN_PATH'] = r'C:\Users\StewM\Documents\BYU Idaho\Fall 2021\programmingCourses\CSE210_team\cse210-student-team-challenges\07-speed\raylib-2.0.0-Win64-mingw\lib'


def main():
    input_service = InputService()
    output_service = OutputService()
    director = Director(input_service, output_service)
    director.start_game()


if __name__ == "__main__":
    main()
