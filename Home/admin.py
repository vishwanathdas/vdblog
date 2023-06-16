from django.contrib import admin
from .models import Contact , About , Privacy , ContactService , HeadOffice, IndiaOffice
# Register your models here.

admin.site.register((Contact , About , Privacy , ContactService , HeadOffice, IndiaOffice))


