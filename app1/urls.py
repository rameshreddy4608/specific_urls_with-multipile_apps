from django.urls import path
from app1.views import *
app_name='something'

urlpatterns=[
    path('ramesh/',ramesh,name='ramesh'),
]