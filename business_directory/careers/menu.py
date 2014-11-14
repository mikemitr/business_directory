from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from .models import Category


class CareersMenu(CMSAttachMenu):
    name = _("Careers Menu")

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        node = NavigationNode(_('Categories'), reverse('categories'), 1)
        nodes.append(node)

        node = NavigationNode(_('Job Posts'), reverse('posts'), 2)
        nodes.append(node)

        return nodes

menu_pool.register_menu(CareersMenu)