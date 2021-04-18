from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User
from .models import CharityUser, Contact
from django import forms

class CharityUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    fname = forms.CharField(max_length=20)
    lname = forms.CharField(max_length=20)
    phone = PhoneNumberField()
    dob = forms.DateField()
    #def clean_field(self): forms.ValidationError("msg")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        contact = Contact.objects.create_contact(self.cleaned_data["fname"],self.cleaned_data["lname"],self.cleaned_data["phone"],self.cleaned_data["dob"])
        user.contact = contact
        if commit:
            user.save()
        return user

    class Meta:
        model = CharityUser
        fields = ('email',)

class CharityUserChangeForm(UserChangeForm):

    class Meta:
        model = CharityUser
        fields = ('email',)