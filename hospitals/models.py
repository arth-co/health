from django.db import models

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

STREAM_CHOICES = (('Allopathic','Allopathic'),
                ('Ayurvedic','Ayurvedic'),
                ('Unani','Unani'),
                ('Siddha','Siddha'),
                ('Homeopathy','Homeopathy'))

class Hospital(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    city = models.CharField(max_length=100,null=False, blank=False)
    address = models.CharField(max_length=200)

    type = models.CharField(max_length=25,null=False, blank=False ,
                  choices=TYPE_CHOICES, default='Charitable')

    stream = models.CharField(max_length=25,null=False, blank=False ,
                  choices=STREAM_CHOICES, default='Allopathic' )

    subsidy = models.CharField(max_length=200,null=False, blank=False)