# Ex02 Django ORM Web Application
## Date: 13.04.2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin

# Register your models here.
from .models import Movie,Mov
admin.site.register(Movie,Mov)

models.py

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




```


## OUTPUT
![alt text](<Screenshot 2025-04-13 151135.png>)

![alt text](<Screenshot 2025-04-13 151204.png>)
## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
