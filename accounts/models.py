from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib import auth
from django.db import models
from CharityConnections.enums import CharityCatagory, CharityAction

from enum import Enum,auto

class MemberType(Enum):
    VOLUNTERR = auto()
    CHARITY = auto()
    def toTuple(self):
        return (self.value,self.name)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

class CharityUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(_('email address'),primary_key=True, blank=False,max_length=155)
    #contact = models.ForeignKey('Contact',on_delete=models.SET_NULL,null=True)
    membertype =  models.IntegerField(choices=([i.toTuple() for i in MemberType]))
    distance = models.IntegerField(null=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.email)

    def fullname(self):
        contact = Contact.objects.get(user=self)
        if(contact ==None):return "No Name"
        return f"{contact.first_name} {contact.last_name}"

    def phone(self):
        contact = Contact.objects.get(user=self)
        if(contact ==None):return "No Phone"
        return f"{contact.phone}"
    def dob(self):
        contact = Contact.objects.get(user=self)
        if(contact ==None):return "No Dob"
        return f"{contact.dob}"

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class ContactManager(models.Manager):
    def create_contact(self,fname,lname,phone,dob):
        contact = self.create(first_name=fname,last_name=lname,phone=phone,dob=dob)
        return contact

class Contact(models.Model):
    user = models.ForeignKey(CharityUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = PhoneNumberField()
    dob = models.DateField()
    objects = ContactManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.phone} | {self.dob}"

class PreferredCategoryManager(models.Manager):
    def create_preferredcategory(self,category,user):
        preferredcategory = self.create(category=category,user=user)
        return preferredcategory
class PreferredCategory(models.Model):
    user = models.ForeignKey(CharityUser,on_delete=models.CASCADE)
    catagory = models.IntegerField(choices=([i.toTuple() for i in CharityCatagory]))

    objects = PreferredCategoryManager()
class PreferredActionManager(models.Manager):
    def create_preferredaction(self,action,user):
        preferredaction = self.create(action=action,user=user)
        return preferredaction
class PreferredAction(models.Model):
    user = models.ForeignKey(CharityUser,on_delete=models.CASCADE)
    action = models.IntegerField(choices=([i.toTuple() for i in CharityAction]))

    objects = PreferredActionManager()