from django.contrib import admin
from pages.models import Page


class PagesAdmin(admin.ModelAdmin):
    save_on_top = True
    list_filter = ['word','content']
    date_hierarchy = 'created'
    list_display = ['word','content' ]
    search_field = ['word','content' ]
admin.site.register(Page , PagesAdmin)
