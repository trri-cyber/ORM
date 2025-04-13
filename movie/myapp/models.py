from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from django.contrib import admin
class Movie(models.Model):
    name=models.CharField(max_length=50,help_text="Name of Movie:")
    date=models.DateField()
    genre=models.CharField(max_length=50,help_text="Genre of Movie:")
    director=models.CharField(max_length=50,help_text="Name of Movie Director:")
    rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

def __str__(self):
        return self.name

class Mov(admin.ModelAdmin):
    list_display=("name","date","genre","director","rating")

