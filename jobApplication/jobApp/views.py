from .models import ApplicantDetailsModel
from django.contrib import messages
from .forms import ApplicationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect

# Class Based Views for the jobApp


class ApplicantsListView(ListView):
    """
    This class view is written for displaying
    the list of records stored in the DB.

    "model" - from which data is to be fetched
    "template_name" - the HTML which shows the list
    """

    model = ApplicantDetailsModel
    template_name = "jobapp/HomePage.html"
    context_object_name = (
        "values"  # the name of iterable used for displaying data in the HTML page
    )

    def get_queryset(self):
        """
        This method will override the existing
        get_queryset() method. By default it will return items in FIFO format.
        This method will now return items in the LIFO format.
        """

        return ApplicantDetailsModel.objects.all().order_by("-id")


class ApplicantCreateView(CreateView):
    """
    This class view is written for adding a new applicant
    or creating a new record in the DB.

    "model" - from which data is to be updated
    "template_name" - the HTML which shows the update form
    "form_class" - the form to recieve data, written in the forms.py file
    "success_url" - redirects to a url on succesfull form submission
    """

    model = ApplicantDetailsModel
    template_name = "jobapp/Form.html"
    form_class = ApplicationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        """This is an inbuilt method used to handle the case where
        form submission is valid. And can be overriden to make custom changes or
         data processing"""

        if form.is_valid():
            """
            The name received should be saved to the DB in the
            proper name format. So the data is processed by using the
            built in methods of Python.

            Here the first_name field is called individually to convert it to a proper
            name format inorder store it to the DB.
            """

            full_name = form.cleaned_data["full_name"]
            proper_full_name = []
            for (
                name
            ) in full_name.split():  # will split the input according to whitespaces
                proper_full_name.append(
                    name.capitalize()
                )  # the name is capitalized and appended to the list
            full_name = " ".join(proper_full_name)
            form.instance.full_name = full_name
            form.save()
            messages.add_message(
                self.request, messages.INFO, "Applicant successfully registered."
            )
            return super().form_valid(form)

    def form_invalid(self, form):
        """
        This is a built in method is to handle the case where the
        form becomes inavlid.
        Here we are overriding it to handle errors according to
        our choice.
        """

        # checking the form, if a non unique email id is given as input
        # if found, an error message is passed
        try:
            if form.errors["email_id"]:
                messages.error(
                    self.request,
                    "Could not register. The given Email ID already exists.",
                )
                return redirect(self.success_url)
        except KeyError:
            pass

        # checking the form, if a non unique phone number is given as input
        # if found, an error message is passed
        try:
            if form.errors["phone_number"]:
                messages.error(
                    self.request,
                    "Could not register. The given Phone number already exists.",
                )
                return redirect(self.success_url)
        except KeyError:
            pass


class ApplicantUpdateView(UpdateView):
    """
    This class view is for updating an existing record in the DB or in this case,
    the applicant who is already registered.
    """

    model = ApplicantDetailsModel
    template_name = "jobapp/UpdateForm.html"
    form_class = ApplicationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        """
        This is a built in method to handle the case where the form is valid.
        If such a record exists it will be updated.
        """

        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            proper_full_name = []
            for name in full_name.split():
                proper_full_name.append(name.capitalize())
            full_name = " ".join(proper_full_name)
            form.instance.full_name = full_name
            form.save()
            messages.add_message(
                self.request, messages.INFO, "Applicant data successfully updated."
            )
            return super().form_valid(form)

    def form_invalid(self, form):
        """
        This is a built in method to handle the case where the form is invalid
        """

        # checking the form, if a non unique email id is given as input for updation
        # if found, an error message is passed
        try:
            if form.errors["email_id"]:
                messages.error(
                    self.request, "Could not update. The given Email ID already exists."
                )
                return redirect(self.success_url)
        except KeyError:
            pass

        # checking the form, if a non unique phone number is given as input for updation
        # if found, an error message is passed
        try:
            if form.errors["phone_number"]:
                messages.error(
                    self.request,
                    "Could not update. The given Phone number already exists.",
                )
                return redirect(self.success_url)
        except KeyError:
            pass


class ApplicantDeleteView(DeleteView):
    """
    This class view is used for deleteing an existing record in the DB or
    in this case deleting an applicant
    """

    model = ApplicantDetailsModel
    template_name = "jobapp/DeletePage.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        """
        This method is to handle the case where form is valid.
        """

        messages.add_message(self.request, messages.INFO, "Applicant deleted.")
        return super().form_valid(form)
