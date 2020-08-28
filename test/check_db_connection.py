from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="80.211.17.161", port=3306, name="addressbook", user="root", password="Too_Borg_23")

l = db.get_contacts_not_in_group(Group(id=200))
for item in l:
    print(item)
print(len(l))
