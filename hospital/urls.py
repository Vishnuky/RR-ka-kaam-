from django.urls import path
from .views import (
    dashboard,
    orders,
    rfid_details,
    scan_logs,
    order_detail
)

app_name = 'hospital'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('orders/', orders, name='orders'),
    path('rfid-details/', rfid_details, name='rfid_details'),  # Changed from 'rfiddetails/' to 'rfid-details/'
    path('scan-logs/', scan_logs, name='scan_logs'),  # Changed from 'scanLogs/' to 'scan-logs/'
    path('order/<int:order_id>/', order_detail, name='order_detail'),
]