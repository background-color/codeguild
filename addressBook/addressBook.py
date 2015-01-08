__author__ = 'root'

book = {name: {in_name: "value",
                phone: "value",
                "alt_phone": "value",
                "address": "value",
                "email": "value"}}

menu_selection = 0
while menu_selection != 5:
    print "Welcome to Your Address Book"
    print "Please choose one of the following:"
    print "1. Create Contact"
    print "2. Edit Contact"
    print "3. View Contact"
    print "4. Delete Contact"
    print "5. Quit Address Book"

    menu_selection = raw_input(">")

    while menu_selection == "1":
        print "Create Contact"
        print "What is the name of the new contact?"
        create_contact = raw_input('>')
        print "Please enter %s's phone number:" % create_contact
        create_phone = raw_input('>')
        print "Please enter %s's alternative phone number:" % create_contact
        create_altPhone = raw_input('>')
        print "Please enter %s's address:"

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
                print "Would you like to edit another contact (e), return to main menu (r) or quit (q)? "
                continue_prompt = raw_input('>')
                if continue_prompt == 'e':
                    print "\n"
                elif continue_prompt == 'q':
                    print "Thanks for playing!"
                    menu_selection = 5
                    break
                else:
                    break

            else:
                break
        else:
            break


    while menu_selection == "3":
        print "View Contact"
        print "Which contact would you like to see?"
        contact_prompt = raw_input('>')
        #need a way to check that contact_prompt is valid.
        print book[contact_prompt]
        print "Would you like to view another contact (v), return to main menu (r) or quit (q)? "
        continue_prompt = raw_input('>')
        if continue_prompt == 'r':
            break
        elif continue_prompt == 'q':
            print "Thanks for playing!"
            menu_selection = 5
            break
        else:
            print "\n"

    # delete contact menu item
    while menu_selection == "4":
        print "Delete Contact"
        print "Which contact would you like to delete?"
        delete_prompt = raw_input('>')
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

