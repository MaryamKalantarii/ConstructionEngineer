from django.contrib import admin
from .models import Order,ContactUs,Team,Skills,Constructions

# Register your models here.
admin.site.register(Team)
admin.site.register(Order)
admin.site.register(ContactUs)
admin.site.register(Skills)
admin.site.register(Constructions)