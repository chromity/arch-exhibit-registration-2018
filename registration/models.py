from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Student(models.Model):
    student_number = models.CharField(max_length=7)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    year_level_choice = (
        ('1ST YEAR', '1ST YEAR'),
        ('2ND YEAR', '2ND YEAR'),
        ('3RD YEAR', '3RD YEAR'),
        ('4TH YEAR', '4TH YEAR'),
        ('5TH YEAR', '5TH YEAR'),
        ('GRADE 11', 'GRADE 11'),
        ('GRADE 12', 'GRADE 12')
    )
    year_level = models.CharField(
        max_length=30,
        choices=year_level_choice,
        default='1ST YEAR',
    )
    program = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
