from django.contrib import admin
from menu.models import MenuItem
from menu.forms import MenuItemForm


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    form = MenuItemForm


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    form = MenuItemForm

admin.site.register(MenuItem, MenuItemAdmin)
