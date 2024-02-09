from django import forms
from .models import Resume, JobListing, ExampleLetter


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["content"]


class ExampleLetterForm(forms.ModelForm):
    class Meta:
        model = ExampleLetter
        fields = ["content"]


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ["description"]


# Optional: Combined form for handling all inputs together
class CombinedForm(forms.Form):
    resume = forms.FileField(label="Upload your resume")
    example_letter = forms.FileField(
        label="Upload an example letter (optional)", required=False
    )
    job_listing_description = forms.CharField(
        widget=forms.Textarea, label="Job listing description"
    )
