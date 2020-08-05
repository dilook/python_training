from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nick=None, mobile_phone=None, work_phone=None,
                 email=None, day=None, month=None, year=None, company=None, address=None, homepage=None, group=None,
                 title=None, id=None):
        self.id = id
        self.title = title
        self.nickname = nick
        self.homepage = homepage
        self.work = work_phone
        self.address = address
        self.new_group = group
        self.company = company
        self.mobile = mobile_phone
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
