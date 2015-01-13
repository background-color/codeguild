__author__ = 'root'

def  main_menu():
    print "Welcome to Your Address Book"
    print "Please choose one of the following:"
    print "1. Create Contact"
    print "2. Edit Contact"
    print "3. View Contact"
    print "4. Delete Contact"
    print "5. Quit Address Book"

def  sub_menu():
    print '-' * 10


book = {}

menu_selection = 0
while menu_selection != 5:
    main_menu()
    menu_selection = raw_input(">")

    # create contact
    while menu_selection == "1":
        print "Create Contact"
        print "Name:"
        create_contact = raw_input('>')
# check if user exists, if yes prompt ' this will overwrite create_contact are you sure (y,n)'
        print "Phone number:"
        create_phone = raw_input('>')
        print "Alternative phone number:"
        create_altPhone = raw_input('>')
        print "Address:"
        create_address = raw_input('>')
        print "Email:"
        create_email = raw_input('>')
        book = {create_contact: {"name": create_contact,
                                 " phone": create_phone,
                                 " alt phone": create_altPhone,
                                 " address": create_address,
                                 " email": create_email}}
# reformat print book so that it looks pretty.
        print book
        print ""
        print("Would you like to create another contact? (y,n)")
        create_prompt = raw_input('>')
        if create_prompt == 'y':
            print "\n"
        else:
            break

# format menu 2 so that it matches the main menu.
# list possible variables to edit as a numbered list with each possible variable.
    while menu_selection == "2":
        print "Edit Contact"
        print "Which contact would you like to edit?"
        edit_contact = raw_input('>')
        print "Are you sure you want to edit %s? (y,n)" % edit_contact
        edit_confirm = raw_input('>')
        if edit_confirm == 'y':
            print "Which field would you like to edit? (name, address, phone, alt_phone, email)"
            edit_field = raw_input('>')
            print "Are you sure you want to edit %s? (y,n)" % edit_field
            edit_field_confirm = raw_input('>')
            if edit_field_confirm == 'y':
                print "What is the new value for %s in contact %s?" % (edit_field, edit_contact)
                new_edit = raw_input('>')
                book = {edit_field: new_edit}
                print book
                print "Would you like to edit another contact (y,n)"
                continue_prompt = raw_input('>')
                if continue_prompt == 'y':
                    print "\n"
                else:
                    break

            else:
                break
        else:
            break

# view contacts
    while menu_selection == "3":
        print "View Contact"
        print "Which contact would you like to see?"
        contact_prompt = raw_input('>')
# need a way to check that contact_prompt is valid.
        print(book[contact_prompt])
        #print("Name:" book[contact_prompt][create_contact])
        print "Would you like to view another contact? (y,n)"
        continue_prompt = raw_input('>')
        if continue_prompt == 'y':
            print "\n"
        else:
            break

# delete contact menu item
    while menu_selection == "4":
        print "Delete Contact"
        print "Which contact would you like to delete?"
        delete_prompt = raw_input('>')
        # check that input is valid
        print "Are you sure you want to remove %s (y,n)" % delete_prompt
        delete_confirm = raw_input('>')
        if delete_confirm == 'y':
            book.pop(delete_prompt)
            print book
            print "Would you like to remove another contact? (y,n)"
            delete_prompt = raw_input('>')
            if delete_prompt == 'y':
                print "\n"
            else:
                print "\n"
                break

        else:
            print "\n"
            break


# quit menu item
    while menu_selection == "5":
        quit_confirm = raw_input("Are you sure you want to quit (y,n)?")
        if quit_confirm == 'y':
            print "Thanks for playing!"
            break
        elif quit_confirm == 'n':
            menu_selection = 0
            break

    if menu_selection == "5":
        break

