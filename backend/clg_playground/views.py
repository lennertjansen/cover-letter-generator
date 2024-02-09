from django.shortcuts import render, redirect
from .forms import CombinedForm


def submit_all(request):
    if request.method == "POST":
        form = CombinedForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data, including saving the job listing text and file uploads
            # Save the resume, example letter, and job listing description
            # Generate or regenerate the cover letter based on the form inputs
            # I assume this is where the openai function will be called
            form.save()
            return redirect(
                "success_url"
            )  # Redirect to a new URL or render a success message
    else:
        form = CombinedForm()
    return render(request, "submit_all.html", {"form": form})
