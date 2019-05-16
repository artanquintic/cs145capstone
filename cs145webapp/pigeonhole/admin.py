from django.contrib import admin
from .models import Owner, Pigeonhole, PigeonholeAction

# Register your models here.
admin.site.register(Pigeonhole)
admin.site.register(Owner)
admin.site.register(PigeonholeAction)
