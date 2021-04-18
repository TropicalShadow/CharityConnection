from django.contrib import admin
from .models import Charity
from accounts.models import Contact
# Register your models here.
@admin.register(Charity)
class CharityAdmin(admin.ModelAdmin):
    fields = ('name','email', 'ein', 'deductibility','url','cause','catagory',)

    def view_contact(self,obj):
        return str(obj.view_contact())
 
    empty_value_display = '???'