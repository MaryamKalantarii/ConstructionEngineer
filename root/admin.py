from django.contrib import admin
from .models import ContactUs,Team,Skills,Constructions, Order_Work,Part

# Register your models here.
admin.site.register(Team)
admin.site.register(Order_Work)
admin.site.register(ContactUs)
admin.site.register(Skills)
admin.site.register(Constructions)
admin.site.register(Part)