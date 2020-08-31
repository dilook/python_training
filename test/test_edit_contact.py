def test_contact_on_edit_form(app, orm):
    contacts_from_home_page = orm.get_contact_list()
    for contact in contacts_from_home_page:
        contact_from_edit_page = app.contact.get_contact_from_edit_page_by_id(contact.id)
        assert contact.firstname == contact_from_edit_page.firstname
        assert contact.lastname == contact_from_edit_page.lastname
        assert contact.email == contact_from_edit_page.email
        assert contact.email2 == contact_from_edit_page.email2
        assert contact.email3 == contact_from_edit_page.email3
        assert contact.mobile_phone == contact_from_edit_page.mobile_phone
        assert contact.work_phone == contact_from_edit_page.work_phone
        assert contact.secondary_phone == contact_from_edit_page.secondary_phone
        assert contact.address == contact_from_edit_page.address
        assert contact.homepage == contact_from_edit_page.homepage
