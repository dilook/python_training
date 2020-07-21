class Contact:
    def __init__(self, first_name, middle_name, last_name, nick,
                 mobile_phone, work_phone, email,
                 day, month, year,
                 company, address, homepage,
                 group, title):
        self.title = title
        self.nick = nick
        self.homepage = homepage
        self.work_phone = work_phone
        self.address = address
        self.group = group
        self.company = company
        self.mobile_phone = mobile_phone
        self.middle_name = middle_name
        self.last_name = last_name
        self.first_name = first_name
        self.year = year
        self.month = month
        self.day = day
        self.email = email
