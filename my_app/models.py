from django.db import models

# Create your models here.
class Person(models.Model):
    GENDER=[
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    ]
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField(default=0,null=True)
    email = models.EmailField()
    # gender = models.CharField(max_length=1, choices=GENDER)

        