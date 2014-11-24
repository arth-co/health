from .forms import HospitalForm, CityForm
import  csv
from django.utils import timezone
from django.contrib.auth.models import User


def import_hospitals(filename):
    rows = open(filename)
    records_added = 0
    errors = []
    admin_user = User.objects.get(username='admin')
    # Generate a dict per row, with the first CSV row being the keys.
    for row in csv.DictReader(rows, delimiter=","):
        print(row)
        # Bind the row data to the MyModelForm
        form = HospitalForm(row)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.created_by = admin_user
            model_instance.edited_by = admin_user
            model_instance.save()

            records_added += 1
        else:
            errors.append(form.errors)

    print(records_added)
    return  errors

def import_cities(filename):
    rows = open(filename)
    records_added = 0
    errors = []
    # Generate a dict per row, with the first CSV row being the keys.
    for row in csv.DictReader(rows, delimiter=","):
        print(row)
        # Bind the row data to the MyModelForm
        form = CityForm(row)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()

            records_added += 1
        else:
            errors.append(form.errors)

    print(records_added)
    return  errors





import django, os
from hospitals.utils import import_cities
django.setup()
filename = os.getcwd() + "\\hospitals\\city_list.csv"
errors = import_cities(filename)
print(errors)