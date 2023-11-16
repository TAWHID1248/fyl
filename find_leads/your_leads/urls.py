from django.urls import path
from . import views



app_name = 'your_leads'

urlpatterns = [
    path('', views.find_leads, name='home'),

]