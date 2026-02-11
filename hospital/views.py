from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def orders(request):
    return render(request, 'orders.html')

def rfid_details(request):
    return render(request, 'rfiddetails.html')

def scan_logs(request):
    return render(request, 'scanLogs.html')

def order_detail(request, order_id):
    return render(request, 'order_detail.html', {'order_id': order_id})
