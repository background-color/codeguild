__author__ = 'root'


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


def print_hangman():
    print('''
            __________
            |/      |
            |      (_)
            |      \|/
            |       |
            |      / \\
            |
           _|__________''')


def print_title():
    print('''
       ___ ___    _____    _______    ________    _____      _____    _______
      /   |   \  /  _  \   \      \  /  _____/   /     \    /  _  \   \      \\
     /    ~    \/  /_\  \  /   |   \/   \  ___  /  \ /  \  /  /_\  \  /   |   \\
     \    Y    /    |    \/    |    \    \_\  \/    Y    \/    |    \/    |    \\
      \___|_  /\____|__  /\____|__  /\______  /\____|__  /\____|__  /\____|__  /
        ''')

print(print_title())
print(print_hangman())
print(print_menu())


