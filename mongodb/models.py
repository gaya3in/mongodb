from djongo import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee(models.Model):
    _id = models.ObjectIdField()
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email_id = models.EmailField(null=False, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(id)
