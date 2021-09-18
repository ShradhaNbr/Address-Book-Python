from contact import Contact


class AddressBook:
    contact_list = []

    def add_contact(self):
        contact = Contact.create_contact()
        self.contact_list.append(contact)

    def display_contact(self):
        contacts = "".join(str(contact) for contact in self.contact_list)
        print(contacts)


if __name__ == "__main__":
    print("*** Welcome to Address Book ***")
    ad = AddressBook()
    ad.add_contact()
    ad.display_contact()
