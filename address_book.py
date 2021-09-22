import logging
import pandas as pd

from contact import Contact

logging.basicConfig(
    filename="address_book.log",
    filemode='w',
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)


class AddressBook:

    def __init__(self):
        self.contact_list = []

    def add_contact(self):
        contact = Contact.create_contact()
        self.contact_list.append(contact)
        df1 = pd.DataFrame({'First Name': [contact.first_name],
                            'Last Name': [contact.last_name],
                            'Address': [contact.address],
                            'City': [contact.city],
                            'State': [contact.state],
                            'Zip': [contact.zip],
                            'Phone Number': [contact.phone_number],
                            'Email': [contact.email]})
        df1.to_csv('address_book.csv', mode='a', header=False, index=False)
        df = pd.read_csv('address_book.csv')
        print(df)

    def display_contact(self):
        contacts = "\n".join(str(contact) for contact in self.contact_list)
        print(contacts)

    def edit_contact(self):
        if len(self.contact_list) == 0:
            print("Contact List is empty")
        else:
            user_data = input("Enter the first name of user you want to edit\n")
            for contact in self.contact_list:
                if contact.first_name == user_data:
                    choice1 = int(input(
                        "Enter what you want to edit \n 1. First Name 2. Last name 3. Address 4. city 5. state 6.zip 7. Phone number 8.Email\n"))
                    if choice1 == 1:
                        first_name = input("Enter new first name\n")
                        contact.first_name = first_name
                    elif choice1 == 2:
                        last_name = input("Enter new last name\n")
                        contact.last_name = last_name
                    elif choice1 == 3:
                        address = input("Enter new address\n")
                        contact.address = address
                    elif choice1 == 4:
                        city = input("Enter new city\n")
                        contact.city = city
                    elif choice1 == 5:
                        state = input("Enter new state\n")
                        contact.state = state
                    elif choice1 == 6:
                        zip = input("Enter new zip\n")
                        contact.zip = zip
                    elif choice1 == 7:
                        phone_number = input("Enter new phone number\n")
                        contact.phone_number = phone_number
                    elif choice1 == 8:
                        email = input("Enter new email\n")
                        contact.email = email
                    else:
                        print("Please enter a valid input")

    def delete_contact(self):
        if len(self.contact_list) == 0:
            print("Contact List is empty")
        else:
            del_contact = input("Enter the name of contact you want to delete\n")
            for contact in self.contact_list:
                if contact.first_name == del_contact:
                    self.contact_list.remove(contact)
                    print("Contact removed successfully")


if __name__ == "__main__":
    print("*** Welcome to Address Book ***")
    ad = AddressBook()
    while True:
        try:
            choice = int(input(
                "Enter what operation you want to perform\n 1.Add Contact 2. Display Contact 3.Edit Contact 4. Delete Contact 5.Exit\n"))
            if choice == 1:
                ad.add_contact()
            elif choice == 2:
                ad.display_contact()
            elif choice == 3:
                ad.edit_contact()
            elif choice == 4:
                ad.delete_contact()
            elif choice == 5:
                print("Successfully closing Address Book")
                exit(0)
            else:
                logging.warning("Invalid option")
        except ValueError:
            logging.warning("Invalid Option selected")
