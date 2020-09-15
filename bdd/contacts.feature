Scenario: Add new contact
  Given a contact list
  Given a contact with <first name>, <last name>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | name  | header  | footer  |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I modify the contact from the list
  Then the new contact list is equal to the old list with the modified group