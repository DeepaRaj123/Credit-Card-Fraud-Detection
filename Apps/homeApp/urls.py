from django.urls import path
from .views import base, login2

urlpatterns = [
    path('', base),
    path('login/', login2, name='login2'),

]
