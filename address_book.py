class AddressBook:

    # This function takes the details for address book from the user
    def create_contact(self):
        first_name = input("Enter first name:\t")
        last_name = input("Enter last name:\t")
        address = input("Enter address:\t")
        city = input("Enter city:\t")
        state = input("Enter state:\t")
        zip = input("Enter zip code:\t")
        phone_number = input("Enter phone number:\t")


if __name__ == "__main__":
    print("*** Welcome to Address Book ***")
    ad = AddressBook()
    ad.create_contact()
