from django.urls import path

app_name ='specific'

from app.views import *

urlpatterns = [
    path('job/',job,name='job')

]