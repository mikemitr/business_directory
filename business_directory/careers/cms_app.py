from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .menu import CareersMenu


class CareerApp(CMSApp):
    name = _("Career App")
    urls = ["careers.urls"]
    menus = [CareersMenu]

apphook_pool.register(CareerApp)
