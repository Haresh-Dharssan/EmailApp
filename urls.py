# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path("", BasicEmailView.as_view(), name='email')

]