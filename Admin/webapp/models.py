from django.db import models

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    username = models.CharField(max_length=255)

    email = models.EmailField(max_length=255)

    phone = models.CharField(max_length=20)

    password = models.CharField(max_length=20)

    
    def __str__(self):

        return self.first_name + "   " + self.last_name











