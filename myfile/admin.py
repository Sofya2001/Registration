from django.contrib import admin
from .models import *

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('login', 'email')
    search_fields = ('login', 'email')









admin.site.register(Registration,RegistrationAdmin )
