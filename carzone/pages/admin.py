from pages.models import Team
from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html

# Register your models here.


class teamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="60">'.format(object.photo.url))
    
    list_display=('id','thumbnail',"first_name","last_name","created_date")
    list_display_links=('first_name',)
    search_fields=("first_name","last_name",'id')
    list_filter=("first_name","last_name",'designation')




admin.site.register(Team,teamAdmin)