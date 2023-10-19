from django import template
from core.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context):
    menu_items = MenuItem.objects.filter(level=1)
    return {
        "menu_items": menu_items,
    }


@register.inclusion_tag('fun/super.html', takes_context=True)
def show_super(context):
    return


@register.inclusion_tag('fun/good.html', takes_context=True)
def show_good(context):
    return