from django.db import models
from django.contrib.sessions.models import Session


class JobListing(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Resume(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    content = models.FileField(upload_to="resumes/")
    created_at = models.DateTimeField(auto_now_add=True)


class ExampleLetter(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    content = models.FileField(upload_to="example_letters/")
    created_at = models.DateTimeField(auto_now_add=True)


class CoverLetter(models.Model):
    resume = models.ForeignKey(
        Resume, related_name="cover_letters", on_delete=models.CASCADE
    )
    job_listing = models.ForeignKey(
        JobListing, related_name="cover_letters", on_delete=models.CASCADE
    )
    example_letter = models.ForeignKey(
        ExampleLetter, related_name="cover_letters", on_delete=models.CASCADE, null=True
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
