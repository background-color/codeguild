__author__ = 'root'
import random


def print_title():
    print('''
       ___ ___    _____    _______    ________    _____      _____    _______
      /   |   \  /  _  \   \      \  /  _____/   /     \    /  _  \   \      \\
     /    ~    \/  /_\  \  /   |   \/   \  ___  /  \ /  \  /  /_\  \  /   |   \\
     \    Y    /    |    \/    |    \    \_\  \/    Y    \/    |    \/    |    \\
      \___|_  /\____|__  /\____|__  /\______  /\____|__  /\____|__  /\____|__  /
        ''')


def print_hangman():
    hangman = '''
            __________
            |/      |
            |      (_)
            |      \|/
            |       |
            |      / \\
            |
           _|__________'''
    return hangman


def print_menu():
    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("1. Play Game")
    print ("2. Rules")
    print ("3. Quit Game")
    print (30 * '-')

    menu_choice = raw_input('>')
    return menu_choice


def show_blanks(secret_word):
    blanks = '_' * len(secret_word)
    return blanks


def guess_letter(correct_letters, incorrect_letters, guessed_letter):
    # Inputs the letter from user and validates the letter.
    check = True
    while check == True:
        print('Please enter a letter to guess: ')
        guessed_letter = raw_input('>')
        guessed_letter = guessed_letter.lower()
        if len(guessed_letter) != 1:
            print('Slow down Romeo, one letter at a time!')
        elif guessed_letter in correct_letters:
            print("That's a good guess, unfortunately you've already guessed that one!")
        elif guessed_letter in incorrect_letters:
            print("That's not a good guess, fortunately you've already guessed that one!")
        elif guessed_letter not in 'abcdefghijklmnopqrstuvwxyz':
            print('What kind of word do you think this is? Letters only, thank you!!')
        else:
            return guessed_letter


def show_board(secret_word, guessed_letter, correct_letters, incorrect_letters, dog):


    #print current_display_word
    # these lines add letters to the correct_list or incorrect_list IF they aren't already there

    for i in secret_word:
        if i in guessed_letter:
            if guessed_letter not in correct_letters and guessed_letter in secret_word:
                correct_letters.append(guessed_letter)
            else:
                pass

        else:
            if guessed_letter not in incorrect_letters and guessed_letter not in secret_word:
                incorrect_letters.append(guessed_letter)
            else:
                pass
    for i in enumerate(secret_word):
        if i[1] == guessed_letter:
            offset = i[0]
            current_display_word[offset] = guessed_letter

    print "".join(current_display_word)
    print "Correct guesses:"
    print correct_letters
    print "Incorrect guesses:"
    print incorrect_letters
    if '_' not in current_display_word:
        print('WINNER, WINNER, CHICKEN DINNER!!!!')
        dog = '5'
        return dog


def random_word():
    word_list = ['ant', 'zebra', 'greg', 'cheese', 'tree',
                 'superb', 'brazil', 'jewelry', 'ant', 'baboon',
                 'badger', 'bat', 'beaver', 'camel', 'cat',
                 'clam', 'cobra', 'cougar', 'coyote', 'crow',
                 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret',
                 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion',
                 'lizard', 'llama', 'mole', 'monkey', 'moose',
                 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda',
                 'parrot', 'pigeon', 'python', 'rabbit', 'ram',
                 'rat', 'raven', 'rhino', 'salmon', 'seal',
                 'shark', 'sheep', 'skunk', 'sloth', 'snake',
                 'spider', 'stork', 'swan', 'tiger', 'toad',
                 'trout', 'turkey', 'turtle', 'weasel', 'whale',
                 'wolf', 'wombat', 'zebra']

    word = (random.choice(word_list))
    return word


def display_board(secret_word, correct_letters, incorrect_letters):
    guessed_letter = raw_input('Please enter a letter to guess: ')
    current_display_word = ''
    for i in secret_word:
        if i in guessed_letter:
            l =  current_display_word + guessed_letter
            current_display_word = current_display_word + guessed_letter
            if guessed_letter not in correct_letters and guessed_letter in secret_word:
                correct_letters.append(guessed_letter)
            else:
                pass

        else:
            current_display_word += '_'
            if guessed_letter not in incorrect_letters and guessed_letter not in secret_word:
                incorrect_letters.append(guessed_letter)
            else:
                pass

    print current_display_word

    print correct_letters
    print incorrect_letters


def play_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


moves_until_hang = 7
correct_letters = []
incorrect_letters = []
guessed_letter = ''
play = True
win_condition = ''
dog = ''
while play == True:

    print_title()
    print(print_hangman())
    menu_option = print_menu()
    secret_word = random_word()
    current_display_word = list(len(secret_word) * "_")


    while menu_option == '1':

        print secret_word



        show_board(secret_word, guessed_letter, correct_letters, incorrect_letters, dog)
        if dog == '5':
            break
        guessed_letter = guess_letter(correct_letters, incorrect_letters, guessed_letter)






