class Contact:

    def __init__(self, contact):
        self.first_name = contact.get("first_name")
        self.last_name = contact.get("last_name")
        self.address = contact.get("address")
        self.city = contact.get("city")
        self.state = contact.get("state")
        self.zip = contact.get("zip")
        self.phone_number = contact.get("phone_number")
        self.email = contact.get("email")

    def __str__(self) -> str:
        return f"First Name = {self.first_name} Last Name = {self.last_name} Address = {self.address} City = {self.city} State = {self.state} Zip = {self.zip} Phone Number = {self.phone_number} Email = {self.email} "

    # This function takes the details for address book from the user
    @staticmethod
    def create_contact():
        first_name = input("Enter first name:\t")
        last_name = input("Enter last name:\t")
        address = input("Enter address:\t")
        city = input("Enter city:\t")
        state = input("Enter state:\t")
        zip = input("Enter zip code:\t")
        phone_number = input("Enter phone number:\t")
        email = input("Enter email id:\t")
        contact_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip,
            "phone_number": phone_number,
            "email": email
        }
        contact = Contact(contact_dict)
        return contact



