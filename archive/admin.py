from django.contrib import admin
from .models import *
# Register your models here.

class SermonAdmin(admin.ModelAdmin): 
  pass
  #fields = ['name', 'pastor', 'verse', 'series', 'date_preached']
  list_display = ('sermon_title', 'pastor' ,'verse', 'series')

admin.site.register(Type)
admin.site.register(Series)
admin.site.register(Sermon, SermonAdmin)
admin.site.register(Featured)
admin.site.register(Pastor)
