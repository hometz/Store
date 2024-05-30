# myapp/models.py

from django.db import models

# Модель Товара
class Product(models.Model):
    UNIT_CHOICES = [
        ('pcs', 'Штуки'),
        ('kg', 'Килограммы'),
        ('l', 'Литры'),
    ]
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES)

    def __str__(self):
        return self.name

# Модель Клиента
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Модель Продажи
class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='SaleProduct')
    sale_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()

    def __str__(self):
        return f"Sale {self.id} to {self.customer}"

# Модель промежуточной таблицы для Sale и Product
class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product} - {self.quantity}"

# Модель адреса для Клиента (Связь Один к Одному)
class CustomerAddress(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name} Address"

class Article(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    summary = models.TextField()
    content = models.TextField(default='')
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    

class Employee(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', default='images/default.jpg')
    job_description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name