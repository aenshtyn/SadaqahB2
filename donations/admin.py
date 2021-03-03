
from django.contrib import admin
from .models import Appeal, Appealer, Donation, Tag
# Register your models here.

admin.site.register(Appealer)
admin.site.register(Appeal)
admin.site.register(Donation)
admin.site.register(Tag)