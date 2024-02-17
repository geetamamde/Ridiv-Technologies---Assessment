from django.db import models

# Create your models here.


class Invoice(models.Model):
    date = models.DateField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Invoice {self.id}: {self.customer_name}"
    

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice Detail {self.id}: {self.description}"