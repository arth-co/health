from django.shortcuts import render, render_to_response, RequestContext
from .forms import HospitalForm
# Create your views here.
def home(request):

    form = HospitalForm(request.POST or None)
    return render_to_response('index.html',
                          locals(),
                          context_instance = RequestContext(request))

# Create your views here.
def test(request):
    return render_to_response('test.html',
                          locals(),
                          context_instance = RequestContext(request))