import warnings

from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from milea_accounts.models import Company, Contact, Type
from milea_base import MILEA_VARS
from milea_base.admin import MileaAdmin


class ContactAdminForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in MILEA_VARS['milea_accounts']['CONTACT_FIELDS_REQUIRED']:
            if field in self.fields:
                self.fields[field].required = True
            else:
                warnings.warn(f"Field name '{field}' in CONTACT_FIELDS_REQUIRED settings does not exist.", Warning)

@admin.register(Contact)
class ContactAdmin(MileaAdmin):

    show_sysdata = True
    list_display = ('verbose_id', 'full_name',)
    readonly_fields = ('full_name',)
    form = ContactAdminForm

    fieldsets = (
        ("", {
            'classes': ('col-lg-12',),
            'fields': (
                'company',
                ('salutation', 'first_name', 'last_name'),
                ('phone', 'email'),
            ),
        }),
    )

@admin.register(Type)
class TypeAdmin(MileaAdmin):

    show_sysdata = True
    list_display = ('as_badge',)
    list_display_links = ('as_badge',)


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0
    min_num = 0
    form = ContactAdminForm

@admin.register(Company)
class CompanyAdmin(MileaAdmin):

    show_sysdata = True
    list_display = ('verbose_id', 'name', 'type_as_badge')
    list_filter = ('type',)
    inlines = [ContactInline]

    fieldsets = (
        ("", {
            'classes': ('col-lg-6',),
            'fields': (
                'name',
                ('street', 'housenumber'),
                ('zip', 'city'),
                ('email', 'phone'),
                ('web', 'vat_number'),
            ),
        }),
        ("", {
            'classes': ('col-lg-6',),
            'fields': (
                'type',
                'logo',
                'notes',
            ),
        }),
    )

    def type_as_badge(self, obj):
        return obj.type.as_badge()
    type_as_badge.short_description = _("Type")
