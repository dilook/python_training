from datetime import datetime

from pony.orm import *

from model.contact import Contact
from model.group import Group


# noinspection PyTypeChecker
class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups",
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        phone = Optional(str, column='phone2')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage = Optional(str, column='homepage')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts",
                     lazy=True)

    def __init__(self, host, port, name, user, password):
        self.db.bind("mysql", host=host, port=port, database=name, user=user, password=password)
        self.db.generate_mapping()

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, footer=group.footer, header=group.header)

        return list(map(convert, groups))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    def convert_contacts_to_model(self, contacts):
        return list(map(convert_contact_to_model, contacts))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_contact_list_with_group(self):
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and c.groups))

    @db_session
    def get_groups_of_contact(self, contact):
        orm_contact = list(select(c for c in ORMFixture.ORMContact if contact.id == c.id))[0]
        return self.convert_groups_to_model(
            select(g for g in ORMFixture.ORMGroup if orm_contact in g.contacts)
        )

    @db_session
    def get_contact_by_id(self, id):
        orm_contact = list(select(c for c in ORMFixture.ORMContact if id == c.id))[0]
        return convert_contact_to_model(orm_contact)


def convert_contact_to_model(contact):
    return Contact(id=str(contact.id),
                   first_name=contact.firstname, last_name=contact.lastname,
                   address=contact.address, homepage=contact.homepage,
                   mobile_phone=contact.mobile, work_phone=contact.work, home_phone=contact.home,
                   secondary_phone=contact.phone,
                   email=contact.email, email2=contact.email2, email3=contact.email3)
