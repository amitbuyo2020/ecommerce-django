from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser, UserProfile

from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser
    list_display = (
        'email', 'username',
        'is_staff', 'is_active'
    )

    list_filter = (
        'email',
        'username'
    )

    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'password1',
                'password2',
                'is_staff',
                'is_active'
            )
        }),
    )

    search_fields = ('email', 'username')
    ordering = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)