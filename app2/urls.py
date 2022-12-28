from django.urls import path
from app2.views import *
app_name='something2'
urlpatterns=[
    path('fun1/',fun1,name='fun1'),
    path('fun2/',fun2,name='fun2'),
]