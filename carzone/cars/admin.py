from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html

# Register your models here.
class carAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40">'.format(object.car_photo.url))
    
    list_display=('id','thumbnail',"car_title","created_date",'is_featured',)
    list_display_links=('car_title',)
    list_editable= ('is_featured',)
    # search_fields=("first_name","last_name",'id')
    # list_filter=("first_name","last_name",'designation')




admin.site.register(Car,carAdmin)