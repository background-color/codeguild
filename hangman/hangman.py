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
    menu_choice = 'n'
    while menu_choice != 'y':
        menu_choice = raw_input("Hey, Would you like to play Hangman? (y,n) ")
        if menu_choice == 'y' or menu_choice == 'Y' or menu_choice == 'yes':
            return 'y'
        elif menu_choice == 'n' or menu_choice == 'N' or menu_choice == 'no':
            quit_menu = raw_input("Do you want to quit?")
            if quit_menu == 'y' or menu_choice == 'Y' or menu_choice == 'yes':
                print("Thanks for playing!")

            break
        else:
            print_menu()


def show_blanks(secret_word):
    blanks = '_' * len(secret_word)
    return blanks


def guess_letter(correct_letters):
    # Inputs the letter from user and validates the letter.
    while True:
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
secret_word = random_word()
correct_letters = ['a']
incorrect_letters = ['b']


print guess_letter(correct_letters)

'''while True:
    #print display_board(secret_word, correct_letters, incorrect_letters)
    for i in range(len(incorrect_letters)):
        print i
        if i >= moves_until_hang:
            print('Your hangman has hung')
            play_again()
'''
'''print(print_hangman())
print(show_blanks(secret_word))
print(secret_word)
print guess_letter(secret_word, correct_letters, incorrect_letters)
print correct_letters
print incorrect_letters'''