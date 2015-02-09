from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.conf import settings
from forms import GeoForm

# Create your views here.
def get_canvas(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GeoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GeoForm()

    return render(request, 'canvas.html', {'geo_form': form})
