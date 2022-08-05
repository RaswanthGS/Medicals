from django.db import models

class Medicals(models.Model):
    Name = models.CharField(max_length=200, blank=False)
    Number = models.IntegerField(blank=False)
    Email_id= models.EmailField()
    Message=models.TextField(max_length=300, blank=False)


    def __str__(self):
        return self.Name

