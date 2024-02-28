from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from milea_base import MILEA_VARS
from milea_base.models import MileaModel

# from django_countries.fields import CountryField


class Company(MileaModel):

    OBJ_VERB_TAG = "KN"

    type = models.ForeignKey('milea_accounts.Type', null=True, on_delete=models.SET_NULL, verbose_name=_("Type"))
    logo = models.ImageField(upload_to='accounts/logos/', null=True, default=None, blank=True, verbose_name=_("Logo"))
    name = models.CharField(max_length=64, unique=True, verbose_name=_("Company name"))
    street = models.CharField(max_length=64, blank=True, verbose_name=_("Street"))
    housenumber = models.CharField(max_length=16, blank=True, verbose_name=_("Housenumber"))
    zip = models.CharField(max_length=16, blank=True, verbose_name=_("ZIP"))
    city = models.CharField(max_length=64, blank=True, verbose_name=_("City"))
    # country = CountryField(blank=True, verbose_name=_("Country"))  # django-countries isnt yet ready for django 5
    phone = models.CharField(max_length=128, blank=True, verbose_name=_("Phone"))
    email = models.EmailField(max_length=128, blank=True, verbose_name=_("E-Mail"))
    web = models.URLField(max_length=128, blank=True, verbose_name=_("Web"))
    notes = models.TextField(blank=True, verbose_name=_("Notes"))
    vat_number = models.CharField(max_length=32, blank=True, verbose_name=_("VAT Number"))
    is_active = None

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")


class Contact(MileaModel):

    OBJ_VERB_TAG = "CT"

    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE, related_name='contacts', verbose_name=_("Company"))
    salutation = models.CharField(max_length=1, blank=True, choices=[('m', _("Male")), ('f', _("Female"))], verbose_name=_("Salutation"))
    first_name = models.CharField(max_length=64, blank=True, verbose_name=_("First name"))
    last_name = models.CharField(max_length=64, blank=True, verbose_name=_("Last name"))
    phone = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("Phone number"))
    email = models.EmailField(max_length=128, blank=True, null=True, db_index=True, verbose_name=_("email address"))
    is_active = None

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    full_name.fget.short_description = _("Full name")

    def clean(self):
        if MILEA_VARS['milea_accounts']['CONTACT_EMAIL_UNIQUE'] and Contact.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError({'email': ["A contact with this email address already exists."]})
        return super().clean()

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['id']
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class Type(MileaModel):

    COLOR_CHOICES = [
        ('cyan', "Cyan"),
        ('azure', "Azure"),
        ('lime', "Lime"),
        ('purple', "Purple"),
    ]

    value = models.CharField(max_length=64, unique=True)
    display = models.CharField(max_length=64)
    color = models.CharField(max_length=16, choices=COLOR_CHOICES)
    is_active = None

    @admin.display
    def as_badge(self):
        return format_html(
            '<span class="badge bg-{} text-{}-fg">{}</span>', self.color, self.color, self.display,
        )
    as_badge.short_description = _("Type")

    def __str__(self):
        return self.display

    class Meta:
        ordering = ['value']
        verbose_name = _("Contact type")
        verbose_name_plural = _("Contact types")
