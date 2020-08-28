from fixture.orm import ORMFixture

db = ORMFixture(host="80.211.17.161", port=3306, name="addressbook", user="root", password="Too_Borg_23")

l = db.get_contact_list()
for item in l:
    print(l)
print(len(l))
