from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Application, Job, Opening, Resume


class JobForm(forms.ModelForm):

    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Job
        exclude = [
            "is_published",
        ]
        # widgets = {"closing_date": DateTimePickerInput()}


class ContactForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)
    from_email = forms.EmailField(label="Your Email", max_length=100)
    subject = forms.CharField(label="Subject", max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ["job"]


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"


class OpeningForm(forms.ModelForm):
    class Meta:
        model = Opening
        fields = "__all__"
