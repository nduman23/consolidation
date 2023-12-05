from django.contrib import admin
from .models import Band

# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ('name','description','image')


admin.site.register(Band,BandAdmin)