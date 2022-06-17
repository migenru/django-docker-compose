from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class CustomUserAdmin(UserAdmin):
    change_form_template = 'accounts/admin/user.html'
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'patronymic', 'last_name', 'email',
                                         'phone')}),

        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'patronymic', 'last_name', 'usergroup', 'is_superuser', )
    list_filter = []

    def usergroup(self, obj):
        return list(obj.groups.all().values_list('name', flat=True))


    usergroup.short_description = 'Группы пользователя'


admin.site.register(User, CustomUserAdmin)
