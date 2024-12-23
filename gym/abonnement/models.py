from django.db import models

# Create your models here.


class Abonnement(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=500)
    email = models.TextField(max_length=50)
    phone = models.TextField(max_length=20)


    def __str__(self):
        return self.name + " -  " +self.phone 