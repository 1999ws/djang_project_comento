from django.contrib import admin
from .models import article

class articleAdmin(admin.ModelAdmin):
    search_fields=['title']
admin.site.register(article,articleAdmin)
# Register your models here.
