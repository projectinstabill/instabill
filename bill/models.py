from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gst = models.CharField(max_length=20)
    adrs = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bill_count = models.IntegerField(blank=True, null=True, default=0)
    cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True, default="")
    acno = models.CharField(max_length=30, blank=True, null=True, default="")
    bank_branch = models.CharField(max_length=50, blank=True, null=True, default="")
    bank_ifsc = models.CharField(max_length=20, blank=True, null=True, default="")


class Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    category = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    acno = models.CharField(max_length=20)
    branch = models.TextField()
    ifsc = models.CharField(max_length=15)
    bal = models.DecimalField(decimal_places=2, max_digits=20)


class FinancialYear(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    from_fy = models.CharField(max_length=5, null=True, blank=True)
    from_to = models.CharField(max_length=5, null=True, blank=True)

   

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gst = models.CharField(max_length=20, blank=True, null=True)
    adrs = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Supplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gst = models.CharField(max_length=20, blank=True, null=True)
    adrs = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

   
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    hsn = models.CharField(max_length=10)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    
class BilledItem(models.Model):
    item_details = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    rate = models.DecimalField(max_digits=20, decimal_places=2)
    sigst = models.DecimalField(max_digits=5, decimal_places=2)
    cgst = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    unit = models.CharField(max_length=5, blank=True, null=True)
    
class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_no=models.PositiveIntegerField(default=0)
    date=models.DateField(blank=True, null=True)
    eway=models.CharField(max_length=25)
    transport=models.CharField(max_length=20)
    vehicle_no=models.CharField(max_length=15)
    invoice_to=models.ForeignKey(Customer , on_delete=models.CASCADE , blank=True, null=True)
    no_of_items=models.PositiveIntegerField(default=0)
    invoice_items=models.ManyToManyField(BilledItem)
    other_charges=models.DecimalField(max_digits=10, decimal_places=2)
    discount=models.DecimalField(max_digits=10, decimal_places=2)
    taxable_amt=models.DecimalField(max_digits=10, decimal_places=2)
    sgst_amt=models.DecimalField(max_digits=10, decimal_places=2)
    cgst_amt=models.DecimalField(max_digits=10, decimal_places=2)
    tgst_amt=models.DecimalField(max_digits=10, decimal_places=2)
    grand_total=models.DecimalField(max_digits=10, decimal_places=2)
    grand_total_words=models.CharField(max_length=150, null=True)

class Payment(models.Model):
    party = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mode = models.CharField(max_length=10)
