import re

from exception import ValidationException


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
        try:
            if re.fullmatch('^[A-Z][a-z]{2,}', first_name):
                first_name = first_name
            else:
                raise ValidationException("First name not valid")
        except ValidationException as e:
            print(e.message)
        last_name = input("Enter last name:\t")
        try:
            if re.fullmatch('^[A-Z][a-z]{2,}', last_name):
                last_name = last_name
            else:
                raise ValidationException("Last name not valid")
        except ValidationException as e:
            print(e.message)
        address = input("Enter address:\t")
        try:
            if re.fullmatch('^[a-zA-Z0-9\\s\\-]{4,}$', address):
                address = address
            else:
                raise ValidationException("Address not valid")
        except ValidationException as e:
            print(e.message)
        city = input("Enter city:\t")
        try:
            if re.fullmatch('^[A-Z][a-z]{2,}', city):
                city = city
            else:
                raise ValidationException("City not valid")
        except ValidationException as e:
            print(e.message)
        state = input("Enter state:\t")
        try:
            if re.fullmatch('^[A-Z][a-z]{2,}', state):
                state = state
            else:
                raise ValidationException("State not valid")
        except ValidationException as e:
            print(e.message)
        zip = input("Enter zip code:\t")
        try:
            if re.fullmatch('^[0-9]{6}', zip):
                zip = zip
            else:
                raise ValidationException("Zip code not valid")
        except ValidationException as e:
            print(e.message)
        phone_number = input("Enter phone number:\t")
        try:
            if re.fullmatch('^[6-9]{1}[0-9]{9}', phone_number):
                phone_number = phone_number
            else:
                raise ValidationException("phone number not valid")
        except ValidationException as e:
            print(e.message)
        email = input("Enter email id:\t")
        try:
            if re.fullmatch('^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$', email):
                email = email
            else:
                raise ValidationException("Email not valid")
        except ValidationException as e:
            print(e.message)

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
