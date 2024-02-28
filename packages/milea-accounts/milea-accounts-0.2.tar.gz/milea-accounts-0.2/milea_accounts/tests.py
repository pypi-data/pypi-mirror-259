from django.core.exceptions import ValidationError
from django.test import TestCase

from milea_base import MILEA_VARS

from .models import Company, Contact, Type


class CompanyModelTest(TestCase):
    def setUp(self):
        # Create a sample Company instance for testing
        self.company = Company.objects.create(name='Test Company')

    def test_company_creation(self):
        # Test if the company is created with the correct name
        self.assertEqual(self.company.name, 'Test Company')

class ContactModelTest(TestCase):
    def setUp(self):
        # Create a sample Contact instance for testing
        self.contact = Contact.objects.create(first_name='John', last_name='Doe')

    def test_contact_creation(self):
        # Test if the contact's full name is correctly formatted
        self.assertEqual(self.contact.full_name, 'John Doe')

    # Test the `clean` method to ensure validation for the email address works properly
    def test_contact_clean_method(self):
        # Create a contact with a unique email address
        contact1 = Contact(first_name='John', last_name='Doe', email='test@example.com')
        contact1.clean()
        contact1.save()

        # Expect a ValidationError when trying to create a contact object with the same email address
        if MILEA_VARS['milea_accounts']['CONTACT_EMAIL_UNIQUE']:
            with self.assertRaises(ValidationError):
                contact2 = Contact(first_name='Jane', last_name='Doe', email='test@example.com')
                contact2.clean()
                contact2.save()

class TypeModelTest(TestCase):
    def setUp(self):
        # Create a sample Type instance for testing
        self.type = Type.objects.create(value='test_value', display='Test Cyan', color='cyan')

    def test_type_creation(self):
        # Test if the type is created with the correct values
        self.assertEqual(self.type.display, 'Test Cyan')
