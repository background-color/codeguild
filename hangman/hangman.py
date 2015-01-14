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


def show_incorrect_letters(incorrect_letters):
    print('Incorrect Letters')
    for letter in incorrect_letters:
        return letter


def guess_letter(secret_word, correct_letters, incorrect_letters):
    # Inputs the letter from user and sorts it into correct or incorrect letter list.
    guessed_letter = raw_input('Please enter a letter to guess: ')
    if secret_word.__contains__(guessed_letter):
        correct_letters.append(guessed_letter)
        return guessed_letter
    else:
        incorrect_letters.append(guessed_letter)
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
moves_until_hang = 7
secret_word = random_word()
correct_letters = []
incorrect_letters = []
print(print_hangman())
print(show_blanks(secret_word))
print(secret_word)
print guess_letter(secret_word, correct_letters, incorrect_letters)
print correct_letters

# print show_missed_letters(missed_letters)
# print(guess_letter())
