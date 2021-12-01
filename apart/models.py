from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# import birthday

# Create your models here.
class Apartment(models.Model):
    name = models.CharField(max_length = 8) #unique=True,
    price = models.IntegerField(default=30000)
    rooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    kitchen = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #this might not be necessary
    # date_created = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.rooms} Room(s), {self.bathrooms} Bathroom(s)-{self.price}"

class Tenant(models.Model):
    name = models.CharField(max_length = 100)
    # dob = birthday.fields.BirthdayField()
    dob = models.DateField() #use a widget to make this look like an html datefield
    #CNI could be an image. upload image of CNI rather than just writing down the number
    CNI = models.CharField(max_length=30)
    phone = models.IntegerField(null=True)
    entry_date = models.DateField() #use this to calculate when the next rent's due, or set due dates to be first day of each month
    apt = models.OneToOneField(Apartment, default=None, blank=True, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f"{self.name}: {self.apt.name}" 