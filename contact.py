class Contact:
    def __init__(self, first_name, middle_name, last_name, b_day):
        self.b_day = b_day
        self.middle_name = middle_name
        self.last_name = last_name
        self.first_name = first_name

    def add_group(self, group):
        self.group = group
        return self

    def add_contact_info(self, contact_info):
        self.contact_info = contact_info


class BDay:
    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day


class ContactInfo:
    def __init__(self, phone, email):
        self.email = email
        self.phone = phone
