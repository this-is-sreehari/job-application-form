from django.db import models
from django.core.exceptions import ValidationError
from datetime import date, datetime
import re

# Create your models here.


class ApplicantDetailsModel(models.Model):
    """
    This class is the actual Model or Table where the data is stored.
    Django will build an actual table using this given data.
    """

    # custom validation function to validata the full_name field
    # allows only alphabets from a to z (including upper and lower)
    # and whitespaces
    def validate_full_name(name):
        full_name_regex = r"^[A-Za-z]+( [A-Za-z]+)?( [A-Za-z]+)?$"
        matchs = re.match(full_name_regex, name)
        if (
            (name == "")
            or (name == None)
            or (matchs is None)
            or (len(name) < 3)
            or len(name) > 75
        ):
            raise ValidationError(
                f"{name} is invalid, it may contain numbers or special chracters"
            )

    # custom validation function to validate the phone_number field
    # allows only digits from 0 to 9
    def validate_phone_number(number):
        phone_pattern = r"^\d{10}$"
        matchs = re.match(phone_pattern, number)
        if (number == "") or (matchs is None):
            raise ValidationError(
                f"{number} is invalid, only digits from 0 to 9 are allowed"
            )

    # custom validation function for date_of_birth
    # allows only applicants who have minimum 18 years of age
    def validate_date_of_birth(dob):
        today = date.today()
        age = (today - dob).days // 365.25
        if dob == "" or dob == None or int(age) < 18:
            raise ValidationError(
                "Invalid Date of Birth, applicant must be minimum 18 years old"
            )

    full_name = models.CharField(
        max_length=75, null=False, validators=[validate_full_name]
    )

    # a list of tuples is given as choice for country_code
    country_code_choices = [
        ("+91", "+91"),
        ("+1", "+1"),
    ]
    country_code = models.CharField(
        max_length=3, null=False, choices=country_code_choices, default="+91"
    )

    phone_number = models.CharField(
        max_length=10, null=False, unique=True, validators=[validate_phone_number]
    )

    email_id = models.EmailField(max_length=254, null=False, unique=True)

    dob = models.DateField(null=False, validators=[validate_date_of_birth])

    # a list of choices for gender
    gender_choices = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    ]
    gender = models.CharField(
        max_length=7, null=True, blank=False, choices=gender_choices, default=None
    )

    # a list of choices for selecting experience in years
    years_choices = [
        ("", "Years"),
        ("0", "Fresher"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("9+", "9+"),
    ]
    years = models.CharField(max_length=2, null=True, blank=True, choices=years_choices)

    # a list of choices for selecting experience in months
    months_choices = [
        ("", "Months"),
        ("0", "Fresher"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("9+", "9+"),
    ]
    months = models.CharField(
        max_length=2, null=True, blank=True, choices=months_choices
    )

    # a list of choices for selecting preferred job role
    job_choices = [
        ("", "Role"),
        ("UI/UX Designer", "UI/UX Designer"),
        ("Front-end Developer", "Front-end Developer"),
        ("Back-end Developer", "Back-end Developer"),
        ("Software Tester", "Software Tester"),
        ("Project Manager", "Project Manager"),
    ]
    job_role = models.CharField(max_length=30, null=False, choices=job_choices)

    address_line_1 = models.CharField(max_length=200, null=True, blank=True)

    address_line_2 = models.CharField(max_length=100, null=True, blank=True)

    city = models.CharField(max_length=30, null=True, blank=True)

    state = models.CharField(max_length=30, null=True, blank=True)

    country = models.CharField(max_length=30, null=True, blank=True)

    zip_code = models.CharField(max_length=6, null=True, blank=True)

    # function to return the Model object with a custom name
    # here it will be in full name

    def __str__(self):
        return self.full_name
