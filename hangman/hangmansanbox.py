__author__ = 'root'
def print_menu():
    print('''
       ___ ___    _____    _______    ________    _____      _____    _______
      /   |   \  /  _  \   \      \  /  _____/   /     \    /  _  \   \      \\
     /    ~    \/  /_\  \  /   |   \/   \  ___  /  \ /  \  /  /_\  \  /   |   \\
     \    Y    /    |    \/    |    \    \_\  \/    Y    \/    |    \/    |    \\
      \___|_  /\____|__  /\____|__  /\______  /\____|__  /\____|__  /\____|__  /
        ''')

    hangman = '''
            __________
            |/      |
            |      (_)
            |      \|/
            |       |
            |      / \\
            |
           _|__________'''
    print hangman

    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("1. Play Game")
    print ("2. Rules")
    print ("3. Quit Game")
    print (30 * '-')

    menu_choice = raw_input('>')
    return menu_choice
menu_choice = print_menu()
print(menu_choice)

if menu_choice == '1':
    print('I hate python')