from django.test import TestCase

from taxi.forms import DriverCreationForm, LicenceUpdateForm


class FormsTest(TestCase):
    def test_driver_creation_form(self):
        form_data = {
            "username": "test",
            "password1": "pass123user",
            "password2": "pass123user",
            "first_name": "Test first",
            "last_name": "Test last",
            "license_number": "TES12345"
        }

        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_correct_license_update_form(self):
        form_data = {
            "license_number": "TES12345"
        }
        form = LicenceUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_incorrect_license_update_form(self):
        form_data = {
            "license_number": "TES123456"
        }
        form = LicenceUpdateForm(data=form_data)

        self.assertFalse(form.is_valid())
