__author__ = 'root'

# TODO: Use pickle to 'pickle' my file.
# Initializing colorama for Windows machines (gotta think about everyone).
from colorama import init
init()
from colorama import Fore, Back, Style

# imports argument variable (argv) from module sys
#from sys import argv

# unpacks the passed in script and assigns it to <filename>
# script, filename = argv

# Creates an object to store our address books. Module to display all contacts
class AddressBook(object):
    # TODO: write docstrings to pep-0257 https://www.python.org/dev/peps/pep-0257/.
    """Stores a

    """
    def __init__(self, owner):
        self.owner = owner
        self.list_of_contacts = {}

    def display_all_contacts(self):
        for key in self.list_of_contacts:
            print key

    def create_contact(self):
        # !self.list_of_contacts [] =
        # TODO: create new contact objects from Contact class


    #def delete_contact(self):
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
        print(Fore.RED + Style.BRIGHT + '-' * 30)
        print(Fore.WHITE + 'First Name: %s' % self.name)
        print(Fore.RED + Style.BRIGHT + '-' * 30)
        print(Fore.WHITE + 'Last Name: %s' % self.last_name)
        print(Fore.RED + Style.BRIGHT + '-' * 30)
        print(Fore.WHITE + 'Phone Number: %s' % self.phone)
        print(Fore.RED + Style.BRIGHT + '-' * 30)
        print(Fore.WHITE + 'Alt. Phone: % s' % self.alt_phone)
        print(Fore.RED + Style.BRIGHT + '-' * 30)
        #TODO: multiple lines for address??
        print(Fore.WHITE + 'Address: % s' % self.address)
        print(Fore.RED + Style.BRIGHT + '-' * 30)
        print(Fore.WHITE + 'Email: %s' % self.email)
        print(Fore.RED + Style.BRIGHT + '-' * 30)
        print(Fore.WHITE + "")

        """
        show all instance attributes
        """

    def edit(self):

        self.name = raw_input(fg + 'Please enter the first name of your contact: ')
        self.last_name = raw_input(fg + 'Please enter the last name of your contact: ')
        self.phone = raw_input(fg + "Please enter %s's phone number: " % first_name)
        self.alt_phone = raw_input(fg + "Please enter an alternative number for %s: " % first_name)
        self.address = raw_input(fg + "Please enter %s's address: " % first_name)
        self.email = raw_input(fg + "Please enter %s's email: " % first_name)




def main_menu(address_book_owner):
    # creates shortcuts for colorama that we are using.
    fg = Fore.GREEN
    fr = Fore.RED
    sra = Style.RESET_ALL
    while True:
        print(Fore.RED + Style.BRIGHT + '-' * 30 + Style.RESET_ALL)
        print "Welcome to Your Address Book"
        print "Please choose one of the following:"
        print "1. List All Contacts"
        print "2. View Individual Contact"
        print "3. Create New Contact"
        print "4. Edit Contact"
        print "5. Delete Contact"
        print "6. Quit Address Book"
        print(Fore.RED + Style.BRIGHT + '-' * 30 + Style.RESET_ALL)

        selection = raw_input(Fore.GREEN + 'What would you like to do? (1-6): ' + Style.RESET_ALL)
        if not selection.isdigit():
            print(Fore.RED + Style.BRIGHT + "DANGER DANGER!!!  That is an invalid selection, 1-6 ONLY!!")
        elif selection.isdigit():
            selection = int(selection)
            if selection > 6 or selection < 1:
                print(Fore.RED + Style.BRIGHT + "DANGER DANGER!!!  That is an invalid selection 1-6 ONLY!! second one")
            elif selection == 1:
                print(address_book_owner.display_all_contacts())
                # TODO: Give user the ability to choose one contact to display.
                test = raw_input(Fore.GREEN + 'Press any key to continue: ')
            elif selection == 2:
                print(Fore.GREEN + 'View Individual Contact: \n')
                # TODO: Prmompt user for which contact and assign that to test_contact.
                # MVP individual_contact = raw_input('Which contact would you like to see?')
                # TODO: Figure out why this returns none as well.
                print(test_contact.display())
                test = raw_input(Fore.GREEN + 'Press any key to continue: ')
            elif selection == 3:
                print(Fore.GREEN + 'Create New Contact' + Style.RESET_ALL)

                # TODO: create a new key for full_name inside of dictionary gregs_contacts.list_of_contacts
                # TODO: instantiate new instance of Contact, named full_name.
                # TODO: give full_name attributes of first_name, last_name,

            elif selection == 6:
                print(Fore.RED + 'Thanks for playing')
                break


# Instantiate an instance of AddressBook named gregs_contacts (note spelling my name wrong was Grant's idea)
# with attributes
gregs_contacts = AddressBook('Gregg')
print gregs_contacts.owner

test_contact = Contacts('Gregg', 'Abbott', '808-280-3799', '503-946-6544',
                       '1631 SE 59th', 'gregg.abbott@gmail.com')

gregs_contacts.list_of_contacts[test_contact.full_name] = test_contact
main_menu(gregs_contacts)


