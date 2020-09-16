Scenario: Add a new contact
  Given a contact list
  Given a contact with <first_name>, <last_name>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | first_name  | last_name   |
  | name1       | last_name1  |
  | name2       | last_name2  |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I modify the contact from the list
  Then the new contact list is equal to the old list with the modified contact