from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MileaAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'milea_accounts'
    verbose_name = _("Accounts")
    menu_icon = "ti ti-address-book"
    menu_firstlvl = ['Company', 'Contact']
    menu_secondlvl = [(_("Configuration"), ['Type'])]
