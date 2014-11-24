from django.contrib import admin
from .models import Hospital, City

# Register your models here.
class HospitalAdmin(admin.ModelAdmin):
    class Meta:
        model = True

class CityAdmin(admin.ModelAdmin):
    class Meta:
        model = True

admin.site.register(City,CityAdmin)
admin.site.register(Hospital,HospitalAdmin)
