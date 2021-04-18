from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .forms import CharityUserCreationForm, CharityUserChangeForm
from .models import CharityUser

class CharityUserAdmin(UserAdmin):
    add_form = CharityUserCreationForm
    form = CharityUserChangeForm
    model = CharityUser
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        #(_('Personal info'), {'fields': ('',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

admin.site.register(CharityUser, CharityUserAdmin)
admin.AdminSite.site_title  = "Charity Connections"
admin.AdminSite.site_header  = "Admin Panel"