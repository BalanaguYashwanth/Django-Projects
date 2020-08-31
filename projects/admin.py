from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(pgdata)
admin.site.register(customerdata)
admin.site.register(memberdata)
admin.site.register(filedata)