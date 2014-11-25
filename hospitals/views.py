from django.shortcuts import render, render_to_response, RequestContext
from .forms import HospitalForm
from django.http import HttpResponse, JsonResponse
from .models import Hospital, City
import json
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

def multi_field_search(request):
    query_text = request.GET.get('term')
    print(query_text)
    hospitals_query = Hospital.objects.filter(name__contains=query_text)
    hospital_list = [{'id':curr.id,
                      'label':curr.name + "," + curr.city,
                      'category':'Hospitals'}
                     for curr in hospitals_query]
    print(json.dumps(hospital_list))
    cities_query = City.objects.filter(name__contains=query_text)
    cities_list = [{'label':curr.name, 'category':'Cities'} for curr in cities_query]
    print(json.dumps(hospital_list + cities_list))
    mimetype = 'application/json'
    return HttpResponse(json.dumps(hospital_list + cities_list),mimetype)

def query_city(request):
    query_text = request.GET.get('term')
    print(request.GET)
    hospitals_query = Hospital.objects.filter(city=query_text)
    hospital_list = [curr.as_dict() for curr in hospitals_query]
    data = {
        'data':hospital_list,
        'columns':Hospital.columns(),
        'columnDefs':Hospital.column_defs()
    }
    mimetype = 'application/json'
    return HttpResponse(json.dumps(data),mimetype)

def query_hospital(request):
    query_text = request.GET.get('id')
    print(query_text)
    hospital = Hospital.objects.get(id=query_text)
    form = HospitalForm(instance=hospital)
    mimetype = 'text/html'
    return HttpResponse(form.as_p(),mimetype)


def submit_form(request):
    form = HospitalForm(request.POST)
    if form.is_valid():
        form.save(commit=False)
    return HttpResponse();