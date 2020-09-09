import getopt
import os
import sys

import jsonpickle

from utils.string_utils import random_string, random_phone, random_site, random_email
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)
    print("\tUse -n to set number of generating contacts\n"
          "\tUse -f to set path to destination file")
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata = [Contact(first_name="", last_name="")] + [
    Contact(first_name=random_string("name", 10), middle_name=random_string("third", 12),
            last_name=random_string("surname", 15), nick=random_string("nick", 10),
            mobile_phone=random_phone(11), work_phone=random_phone(11), secondary_phone=random_phone(11),
            home_phone=random_phone(11), email=random_email(15), email2=random_email(15), email3=random_email(15),
            day="1", month="April", year="1978", company=random_string("surname", 10),
            address=random_string("addr", 56),
            homepage=random_site(16), title=random_string("surname", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as test_data:
    test_data.write(jsonpickle.encode(testdata, indent=2))
