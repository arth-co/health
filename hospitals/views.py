from django.shortcuts import render, render_to_response, RequestContext
from .forms import HospitalForm
from django.http import HttpResponse, JsonResponse
from .models import Hospital, City
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.html import mark_safe
import json

# Create your views here.
def home(request):

    form = HospitalForm(request.POST or None)
    city_list = mark_safe(City.get_list())
    return render_to_response('index.html',
                          locals(),
                          context_instance = RequestContext(request))

# Create your views here.
def test(request):
    return render_to_response('test.html',
                          locals(),
                          context_instance = RequestContext(request))


def query_hospital_multi_term(query_text):
    query_terms = query_text.split(' ')
    query = Q()
    for curr in query_terms:
        query = query & (Q(city__icontains=curr)|Q(name__icontains=curr))

    return Hospital.objects.filter(query)[:10]


def multi_field_search(request):
    query_text = request.GET.get('term')
    hospitals_query = query_hospital_multi_term(query_text)
    hospital_list = [{'data':curr.as_dict(),
                      'label':curr.name + "," + curr.city,
                      'category':'Hospitals'}
                     for curr in hospitals_query]
    print(json.dumps(hospital_list))

    # Search through the City Database
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

def query_similar_hospitals(request):
    query_text = request.GET.get('term')
    hospitals_query = query_hospital_multi_term(query_text)
    hospital_list = [{'data':curr.as_dict(),
                      'label':curr.name + "," + curr.city,
                      'category':'Similar Hospitals'}
                     for curr in hospitals_query]
    print(json.dumps(hospital_list))
    mimetype = 'application/json'
    return HttpResponse(json.dumps(hospital_list),mimetype)

    '''
    query_text = request.GET.get('term')
    print(query_text)
    hospitals_query = Hospital.objects.get(name__contains=query_text)
    hospital_list = [{'data':curr.as_dict(),
                      'label':curr.name + "," + curr.city,
                      'category':'Hospitals'}
                     for curr in hospitals_query]
    return HttpResponse(json.dumps(hospital_list ),'application/json')
'''


def submit_form(request):
    try:
        print(request.POST)
        pk = request.POST.get('pk')

        if int(pk) is not -1:
            model_instance = Hospital.objects.get(pk=pk)
            form = HospitalForm(request.POST, instance=model_instance)
            if form.is_valid():
                model_instance.modified_by = request.user
                model_instance.save()
            return HttpResponse()
        else:
            form = HospitalForm(request.POST)
            if form.is_valid():
                print('Form was valid')
                model_instance = form.save(commit=False)
                model_instance.created_by = User.objects.get(username='admin')
                model_instance.edited_by = User.objects.get(username='admin')
                model_instance.save()
                return HttpResponse()
    except:
        raise LookupError