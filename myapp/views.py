# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Customer, Sale, SaleProduct, CustomerAddress, Article, FAQ, Employee
from .forms import ProductForm, CustomerForm, SaleForm, SaleProductForm, CustomerAddressForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.http import HttpResponseForbidden

# Представления для модели Product
# Create
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'myapp/product_form.html', {'form': form})

# Read
def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'myapp/product_detail.html', {'product': product})

# Update
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp/product_form.html', {'form': form})

# Delete
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'myapp/product_confirm_delete.html', {'product': product})

# Представления для модели Customer
# Create
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'myapp/customer_form.html', {'form': form})

# Read
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'myapp/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'myapp/customer_detail.html', {'customer': customer})

# Update
def update_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', pk=pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'myapp/customer_form.html', {'form': form})

# Delete
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'myapp/customer_confirm_delete.html', {'customer': customer})

# Представления для модели Sale
# Create
def create_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'myapp/sale_form.html', {'form': form})

# Read
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'myapp/sale_list.html', {'sales': sales})

def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, 'myapp/sale_detail.html', {'sale': sale})

# Update
def update_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sale_detail', pk=pk)
    else:
        form = SaleForm(instance=sale)
    return render(request, 'myapp/sale_form.html', {'form': form})

# Delete
def delete_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        sale.delete()
        return redirect('sale_list')
    return render(request, 'myapp/sale_confirm_delete.html', {'sale': sale})

# Представления для модели SaleProduct
# Create
def create_sale_product(request):
    if request.method == 'POST':
        form = SaleProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_product_list')
    else:
        form = SaleProductForm()
    return render(request, 'myapp/sale_product_form.html', {'form': form})

# Read
def sale_product_list(request):
    sale_products = SaleProduct.objects.all()
    return render(request, 'myapp/sale_product_list.html', {'sale_products': sale_products})

def sale_product_detail(request, pk):
    sale_product = get_object_or_404(SaleProduct, pk=pk)
    return render(request, 'myapp/sale_product_detail.html', {'sale_product': sale_product})

# Update
def update_sale_product(request, pk):
    sale_product = get_object_or_404(SaleProduct, pk=pk)
    if request.method == 'POST':
        form = SaleProductForm(request.POST, instance=sale_product)
        if form.is_valid():
            form.save()
            return redirect('sale_product_detail', pk=pk)
    else:
        form = SaleProductForm(instance=sale_product)
    return render(request, 'myapp/sale_product_form.html', {'form': form})

# Delete
def delete_sale_product(request, pk):
    sale_product = get_object_or_404(SaleProduct, pk=pk)
    if request.method == 'POST':
        sale_product.delete()
        return redirect('sale_product_list')
    return render(request, 'myapp/sale_product_confirm_delete.html', {'sale_product': sale_product})

# Представления для модели CustomerAddress
# Create
def create_customer_address(request):
    if request.method == 'POST':
        form = CustomerAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_address_list')
    else:
        form = CustomerAddressForm()
    return render(request, 'myapp/customer_address_form.html', {'form': form})

# Read
def customer_address_list(request):
    customer_addresses = CustomerAddress.objects.all()
    return render(request, 'myapp/customer_address_list.html', {'customer_addresses': customer_addresses})

def customer_address_detail(request, pk):
    customer_address = get_object_or_404(CustomerAddress, pk=pk)
    return render(request, 'myapp/customer_address_detail.html', {'customer_address': customer_address})

# Update
def update_customer_address(request, pk):
    customer_address = get_object_or_404(CustomerAddress, pk=pk)
    if request.method == 'POST':
        form = CustomerAddressForm(request.POST, instance=customer_address)
        if form.is_valid():
            form.save()
            return redirect('customer_address_detail', pk=pk)
    else:
        form = CustomerAddressForm(instance=customer_address)
    return render(request, 'myapp/customer_address_form.html', {'form': form})

# Delete
def delete_customer_address(request, pk):
    customer_address = get_object_or_404(CustomerAddress, pk=pk)
    if request.method == 'POST':
        customer_address.delete()
        return redirect('customer_address_list')
    return render(request, 'myapp/customer_address_confirm_delete.html', {'customer_address': customer_address})

def latest_article(request):
    latest_article = Article.objects.latest('publication_date')
    return render(request, 'latest_article.html', {'article': latest_article, 'user': request.user})

def about_us(request):
    return render(request, 'about_us.html', {'user': request.user})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles, 'user': request.user})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

def faq_list(request):
    faqs = FAQ.objects.all().order_by('-date_added')
    return render(request, 'faq_list.html', {'faqs': faqs, 'user': request.user})

def contact_list(request):
    employees = Employee.objects.all()
    return render(request, 'contact_list.html', {'employees': employees, 'user': request.user})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('about_us')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def admin_required(view_func):
    
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden()
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Примените этот декоратор к вашим представлениям

@admin_required
def admin_page(request):
    return render(request, 'admin_page.html')
