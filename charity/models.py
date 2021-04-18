from accounts.models import Contact
from django.db import models
from enum import Enum,auto

class CharityCatagory(Enum):
    PERSON = auto()
    HEALTH = auto()
    ANIMALS = auto()
    ENVIRONMENT = auto()
    EDUCATION = auto()

    def toTuple(self):
        return (self.value,self.name)


class Charity(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    ein = models.CharField(max_length=10)
    deductibility = models.BooleanField()
    url = models.URLField()
    cause = models.TextField(max_length=100)
    catagory = models.IntegerField(choices=([i.toTuple() for i in CharityCatagory]))

    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"<Charity {self.email}>"

    def view_contact(self):
        return f'{self.contact.first_name} {self.contact.last_name} |  {self.contact.phone} | {self.contact.dob}'
