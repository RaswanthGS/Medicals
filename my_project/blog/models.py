from django.db import models

class Medicals(models.Model):
    Name = models.TextField(max_length=200, blank=False)
    Number = models.IntegerField(blank=False)
    Email_id= models.EmailField()
    Message=models.CharField(max_length=300, blank=False)
    photo = models.ImageField()


    def __str__(self):
        return self.Name

