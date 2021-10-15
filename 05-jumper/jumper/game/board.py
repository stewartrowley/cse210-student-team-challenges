class board:
    def display_word():
        letter = []
        for letter in len(word):
            display += '_'
            print(display)
        for position in range(len(word)):
            letter = word[position]
            if guess == True:
                display[position] = letter
            else:
                print(display)

    def display_jumper():
        if guess == false:
            parachute_display = ''
        elif


