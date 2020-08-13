from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nick=None, mobile_phone=None, work_phone=None,
                 email=None, day=None, month=None, year=None, company=None, address=None, homepage=None, group=None,
                 title=None, id=None, all_phones=None, home_phone=None, secondary_phone=None, email2=None, email3=None,
                 all_emails=None):
        self.all_emails = all_emails
        self.email3 = email3
        self.email2 = email2
        self.secondary_phone = secondary_phone
        self.home_phone = home_phone
        self.all_phones = all_phones
        self.id = id
        self.title = title
        self.nickname = nick
        self.homepage = homepage
        self.work_phone = work_phone
        self.address = address
        self.new_group = group
        self.company = company
        self.mobile_phone = mobile_phone
        self.middlename = middle_name
        self.lastname = last_name
        self.firstname = first_name
        self.byear = year
        self.bmonth = month
        self.bday = day
        self.email = email

    def __repr__(self):
        return "%s: %s, %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) \
               and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def get_id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
