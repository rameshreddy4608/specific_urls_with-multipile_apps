from django.urls import path
from app2.views import *
app_name='nothing'

urlpatterns=[
    path('rupesh/',rupesh,name='rupesh')
]