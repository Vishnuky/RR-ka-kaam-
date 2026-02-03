from django.urls import path
from .views import dashboard

app_name = 'hospital'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]
