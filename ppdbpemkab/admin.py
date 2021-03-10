from django.contrib import admin

# Register your models here.

from .models import DataSiswa, UserSiswa

admin.site.register(DataSiswa)
admin.site.register(UserSiswa)