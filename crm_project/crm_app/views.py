from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer, Invoice
from .utils import send_whatsapp_message

def index(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        email=data.get('email')
        customer= Customer.objects.create(name=name, email=email)
        return JsonResponse({'id': customer.id, 'name':customer.name})
    
def create_invoice(request):
    if request.method=='POST':
        data=request.POST
        customer_id=data.get('customer_id')
        amount=data.get('amount')
        invoice= Invoice.objects.create(customer_id=customer_id, amount=amount)
        return JsonResponse({'id': invoice.id, 'amount':invoice.amount})
    
def send_message(request):
    if request.method=='POST':
        data= request.POST
        phone_number=data.get('phone_number')
        message=data.get('message')
        response=send_whatsapp_message(phone_number, message)
        return JsonResponse(response)