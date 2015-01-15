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

game = True
while game:
    menu_choice = print_menu()
    if menu_choice == '1':
        print('g')
    elif menu_choice =='2':
        print('THE RULES:::')
        print('_' * 30)
        print(''' The Computer acts as executioner and YOU, the player are to be executed.
    You have one last chance at a stay of execution. Guess the word before you run out of
    body parts. Good Luck!!!''')
        print ('_' * 30)
        any_key = raw_input('Press any key to continue')
        if any_key:
            break
    elif menu_choice == '3':
        print('Thanks For Playing!!!')
        game = False