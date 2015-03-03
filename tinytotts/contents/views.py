from django.shortcuts import render
from contents.forms import ContentTypeForm

def add_contenttype(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = ContentTypeForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return render(request, 'base/index.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ContentTypeForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'contents/add_contenttype.html', {'form': form})
