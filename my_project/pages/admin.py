from django.contrib import admin
from .models import article
# Register your models here.
class articleAdmin(admin.ModelAdmin):
    search_fields=['title']
admin.site.register(article,articleAdmin)