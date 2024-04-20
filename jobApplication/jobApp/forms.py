from django.forms import ModelForm, TextInput, EmailInput, Select, widgets, RadioSelect
from .models import ApplicantDetailsModel


class ApplicationForm(ModelForm):
    """
    This class is created by inheriting the ModelForm class.
    The given model will be converted to a form by using this method.
    """

    # Meta class is used to control the behaviour the model
    class Meta:
        # the model to store data and create the form
        model = ApplicantDetailsModel

        # the fields to take input
        fields = "__all__"

        # the label of each field
        labels = {
            "full_name": "Full Name",
            "phone_number": "Contact",
            "email_id": "Email ID",
            "dob": "Date Of Birth",
            "gender": "Gender",
            "years": "Experience",
            "job_role": "Preferred Role",
            "address_line_1": "Address",
        }

        # declaring the input element for each field
        widgets = {
            "full_name": TextInput(
                attrs={"class": "full_name", "placeholder": "Enter your full name"}
            ),
            "country_code": Select(
                attrs={
                    "class": "country_code",
                }
            ),
            "phone_number": TextInput(
                attrs={
                    "class": "phone_number",
                    "placeholder": "Enter your contact number",
                }
            ),
            "email_id": EmailInput(
                attrs={"class": "email_id", "placeholder": "Enter your Email ID"}
            ),
            "dob": widgets.DateInput(
                attrs={
                    "class": "dob",
                    "type": "date",
                }
            ),
            "gender": RadioSelect(attrs={"class": "gender"}),
            "years": Select(attrs={"class": "years"}),
            "months": Select(attrs={"class": "months"}),
            "job_role": Select(attrs={"class": "job_role"}),
            "address_line_1": TextInput(
                attrs={"class": "address_fields", "placeholder": "Address Line 1"}
            ),
            "address_line_2": TextInput(
                attrs={"class": "address_fields", "placeholder": "Address Line 2"}
            ),
            "city": TextInput(
                attrs={"class": "address_fields", "placeholder": "District"}
            ),
            "state": TextInput(
                attrs={"class": "address_fields", "placeholder": "State"}
            ),
            "country": TextInput(
                attrs={"class": "address_fields", "placeholder": "Country"}
            ),
            "zip_code": TextInput(
                attrs={"class": "address_fields", "placeholder": "Zip code"}
            ),
        }
