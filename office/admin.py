from django.contrib import admin
from .models import *

admin.site.register(Company)
admin.site.register(Country)
admin.site.register(Currency)
admin.site.register(Group)
admin.site.register(LegalForm)
admin.site.register(Nationality)

# Register your models here.
