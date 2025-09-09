from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name
class Invoice(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=20, default='Bekleyen')

    def __str__(self):
        return f'Fatura {self.id} numaralı {self.customer.name} kişisine ait fatura'