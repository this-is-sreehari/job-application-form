from django.contrib import admin
from .models import ApplicantDetailsModel
# Register your models here.

class ApplicantsDisplay(admin.ModelAdmin):
    """
    A class for displaying the model with ceratin fields
    given as a tuple.
    """

    # tuple to display fields in admin page
    list_display = ("full_name", "country_code", "phone_number", "email_id", "job_role")

# to display Model in admin page 
admin.site.register(ApplicantDetailsModel, ApplicantsDisplay)
