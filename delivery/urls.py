from django.urls import path
from .views import dashboard

app_name = 'delivery'

urlpatterns = [
    path('delivery/', dashboard, name='deliveryDashboard'),
]
