from django.urls import path
from .views import *


app_name = 'services'

urlpatterns = [
    path("",services, name='services'),
    path("service-detail/",service_detail,name="service_detail"),
]