# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Customer, Sale, SaleProduct, CustomerAddress, Article, FAQ, Employee
#from .forms import 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ProductEdit, SaleProductForm
from django.utils import timezone

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products, 'user': request.user})

def create_product(request):
    if request.method == 'POST':
        form = ProductEdit(request.POST)
        if form.is_valid():
            product = Product(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                unit=form.cleaned_data['unit']
            )
            product.save()
            return redirect('products_list')
    else:
        form = ProductEdit()
    return render(request, 'create_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductEdit(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.unit = form.cleaned_data['unit']
            product.save()
            return redirect('products_list')
    else:
        form = ProductEdit(initial={'name': product.name, 'price': product.price})
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('products_list')

def buy_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = SaleProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            sale_product = SaleProduct.objects.create(product=product, quantity=quantity)
            
            customer = request.user.customer
            sale, created = Sale.objects.get_or_create(customer=customer)
            
            sale.sale_date = timezone.now()
            sale.delivery_date = sale.sale_date + timezone.timedelta(days=7)
            sale.save()
            
            sale.products.add(sale_product)
            return redirect('products_list')
    else:
        form = SaleProductForm()
    return render(request, 'buy_product.html', {'form': form, 'product': product})


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
            return redirect('about_us')
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