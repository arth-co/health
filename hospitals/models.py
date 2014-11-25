from django.db import models
from django.contrib.auth.models import User

SPECIALITY_CHOICES = (('General - Multispeciality','General - Multispeciality'),
( 'Eye - Ophthalmology', 'Eye - Ophthalmology'),
(' Heart - Cardiology',' Heart - Cardiology'),
(' Cancer - Oncology',' Cancer - Oncology'),
('Bones - Orthopaedic','Bones - Orthopaedic'),
(' Neurology',' Neurology'),
(' Dental',' Dental'),
(' Ear Nose Throat',' Ear Nose Throat'),
(' Kidney',' Kidney'),
(' Children - Paediatrics',' Children - Paediatrics'),
(' Emergency',' Emergency'),
(' Maternity',' Maternity'),
(' Mental',' Mental'),
(' Psychiatric',' Psychiatric'),
(' Veterinary',' Veterinary'),
)

TYPE_CHOICES = (('Charitable','Charitable'),
                ('Government','Government'),
                ('Private','Private'))

STREAM_CHOICES = (('Allopathy','Allopathy'),
                ('Ayurveda','Ayurveda'),
                ('Unani','Unani'),
                ('Siddha','Siddha'),
                ('Homeopathy','Homeopathy'))


class City(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    def __str__(self):
        return str(self.name)

class Hospital(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    city = models.CharField(max_length=100,null=False, blank=False)
    address = models.CharField(max_length=200,blank=True)

    type = models.CharField(max_length=25,
                  choices=TYPE_CHOICES, default='Charitable',blank=True)

    speciality = models.CharField(max_length=25,
                  choices=SPECIALITY_CHOICES, default='Allopathic' ,blank=True)

    stream = models.CharField(max_length=25,
                  choices=STREAM_CHOICES, default='General - MultiSpeciality' ,blank=True)

    subsidy = models.CharField(max_length=200, blank=True)
    created_by = models.ForeignKey(User, related_name='created_by')
    edited_by  = models.ForeignKey(User, related_name='edited_by')
    created_on = models.DateTimeField(editable=False, auto_now_add=True,null=True, blank=True)
    modified_on = models.DateTimeField(editable=False,auto_now=True,null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def as_dict(self):
        return {
            'pk':self.pk,
            'name': self.name,
            'city':self.city,
            'address':self.address,
            'type':self.type,
            'speciality':self.speciality,
            'stream':self.stream,
            'subsidy':self.subsidy,
            # other stuff
        }

    def as_list(self):
        return [
            self.pk,
            self.name,
            self.city,
            #self.address,
            self.type,
            self.speciality,
            self.stream,
            self.subsidy
        ]
    @staticmethod
    def columns():
        return [
            {'data':'pk',
             'title':'PK',
             },
            {'data':'name',
             'title':'Name'},
            {'data':'city',
             'title':'City'},
            {'data':'type',
             'title':'Type'},
            {'data':'speciality',
             'title':'Speciality'},
            {'data':'stream',
             'title':'Stream'},
            {'data':'subsidy',
             'title':'Subsidy'}
        ]
    @staticmethod
    def column_defs():
        return [
            {'targets':[0],
             'visible':False,
             'searchable':False},
        ]
