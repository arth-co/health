from django.contrib import admin
from .models import Hospital

# Register your models here.
class HospitalAdmin(admin.ModelAdmin):
    class Meta:
        model = True

admin.site.register(Hospital,HospitalAdmin)