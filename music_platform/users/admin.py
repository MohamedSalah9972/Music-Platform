from django.contrib import admin
from .models import CustomUser
from django import forms


class AdminCustomUser(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(AdminCustomUser, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'bio':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

    pass


admin.site.register(CustomUser, AdminCustomUser)
