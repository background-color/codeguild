__author__ = 'root'
# Initializing colorama for Windows machines (gotta think about everyone).
from colorama import init
init()
from colorama import Fore, Back, Style

# imports argument variable (argv) from module sys
#from sys import argv

# unpacks the passed in script and assigns it to <filename>
#script, filename = argv

# Creates an object to store our address books. Module to display all contacts
class AddressBook(object):
    def __init__(self, owner):
        self.owner = owner
        self.list_of_contacts = {}

    def display_all_contacts(self):
        for key in self.list_of_contacts:
            print key
        #print(gregs_contacts.list_of_contacts.keys())


    def create_contact(self):
        """
        create new contact objects from Contact class
        """

    def delete_contact(self):
        """
        select an exiting contact object
        delete the selected contact object
        """


class Contacts(object):

    def __init__(self, name, last_name, phone, alt_phone, address, email):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.alt_phone = alt_phone
        self.address = address
        self.email = email
        self.full_name = self.name + " " + self.last_name

    def display(self):
        print(Fore.RED + '-' * 30)
        print(Fore.WHITE + Style.BRIGHT + "%s %s" % (self.name.upper(), self.last_name.upper()))
        print(Fore.RED + '-' * 30)
        print(Fore.WHITE + 'First Name: %s' % self.name)
        print(Fore.RED + '-' * 30)
        print(Fore.WHITE + 'Last Name: %s' % self.last_name)
        print(Fore.RED + '-' * 30)
        print(Fore.WHITE + 'Phone Number: %s' % self.phone)
        print(Fore.RED + '-' * 30)
        print(Fore.WHITE + 'Alt. Phone: % s' % self.alt_phone)
        print(Fore.RED + '-' * 30)
        #TODO: multiple lines for address??
        print(Fore.WHITE + 'Address: % s' % self.address)
        print(Fore.RED + '-' * 30)
        print(Fore.WHITE + 'Email: %s' % self.email)
        print(Fore.RED + '-' * 30)
        print(Fore.WHITE + "")

        """
        show all instance attributes
        """

    def edit(self):
        """
        show current instance attribute values
        allow for editing of those values
        """



def main_menu():
    print(Fore.RED + '-' * 30)
    print "Welcome to Your Address Book"
    print "Please choose one of the following:"
    print "1. Create Contact"
    print "2. Edit Contact"
    print "3. View Contact"
    print "4. Delete Contact"
    print "5. Quit Address Book"
    print(Fore.RED + '-' * 30)

    selection = raw_input('What would you like to do? (1-5): ')
    if selection == '5':
        return selection
    elif selection == '2':
        print('Thanks for playing')


gregs_contacts = AddressBook('Gregg')
print gregs_contacts.owner

test_contact = Contacts('Gregg', 'Abbott', '808-280-3799', '503-946-6544',
                       '1631 SE 59th', 'gregg.abbott@gmail.com')

gregs_contacts.list_of_contacts[test_contact.full_name] = test_contact

test_contact.display()
#print(gregs_contacts.list_of_contacts.keys())
gregs_contacts.display_all_contacts()


'''
def sub_menu():
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
        break'''

'''Person.name = raw_input('please enter a name: ')
print(Person.name)
Person.phone = raw_input('please enter a phone number: ')
print(Person.phone)
Person.alt_phone = raw_input('please enter an alt phone number: ')
print(Person.alt_phone)
Person.address = raw_input('please enter an address: ')
print(Person.address)
Person.email = raw_input('please enter an email: ')
print(Person.email)
'''