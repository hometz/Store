
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Customer, Sale, SaleProduct, CustomerAddress, Article, FAQ, Employee, Review, PromoCode
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ProductEdit, SaleProductForm, ReviewForm
import requests
from django.utils import timezone
import matplotlib.pyplot as plt
import os
from django.db.models import Sum
from decimal import Decimal


def get_random_gif():
    api_key = 'Eio5GQwmcuMOFpcd811Iu4fvlUBVjVDN'
    url = f'https://api.giphy.com/v1/gifs/random?api_key={api_key}&rating=g'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['data']['images']['original']['url']
    except requests.exceptions.RequestException as e:
        print(f"Giphy API error: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing Giphy API response: {e}")
        return None


def get_cat_fact():
    url = 'https://catfact.ninja/fact'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['fact']
    except requests.exceptions.RequestException as e:
        print(f"Cat Facts API error: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing Cat Facts API response: {e}")
        return None



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products, 'user': request.user})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product, 'user': request.user})

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

def buy_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = SaleProductForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            quantity = form.cleaned_data['quantity']
            promo_code = form.cleaned_data.get('promo_code')
            
            customer, created = Customer.objects.get_or_create(
                email=email,
                defaults={'first_name': first_name, 'last_name': last_name, 'phone': phone}
            )
            
            sale = Sale.objects.create(
                customer=customer,
                delivery_date=timezone.now() + timezone.timedelta(days=7) 
            )
            
            # Применяем скидку, если указан промокод
            discount = Decimal('0.00')
            if promo_code:
                try:
                    promo = PromoCode.objects.get(code=promo_code, active=True)
                    discount = Decimal(promo.discount_percent) / Decimal(100)
                except PromoCode.DoesNotExist:
                    pass

            # Вычисляем цену с учетом скидки
            price_with_discount = product.price - (product.price * discount)

            SaleProduct.objects.create(
                sale=sale,
                product=product,
                quantity=quantity,
                price=price_with_discount  # Учитываем скидку при установке цены товара
            )
            
            # Обновляем общую цену заказа
            sale.total_price = price_with_discount * quantity
            sale.save()
            
            return redirect('products_list')
    else:
        form = SaleProductForm()
    return render(request, 'buy_product.html', {'form': form, 'product': product})


def sale_list(request):
    sales = Sale.objects.all().prefetch_related('products', 'customer')
    
    sales_by_customer = SaleProduct.objects.values('sale__customer').annotate(total_quantity=Sum('quantity'))
    
    customers = []
    total_quantity = []
    for sale in sales_by_customer:
        customer = Customer.objects.get(pk=sale['sale__customer'])
        customers.append(customer)
        total_quantity.append(sale['total_quantity'])
    
    customer_names = [f"{customer.first_name} {customer.last_name}" for customer in customers]
    
    plt.bar(range(len(customers)), total_quantity)
    plt.xlabel('Клиент')
    plt.ylabel('Общее количество продуктов')
    plt.title('Статистика продаж по клиентам')
    plt.xticks(range(len(customers)), customer_names, rotation=45, ha='right')
    plt.tight_layout()
    
    chart_path = os.path.join('media', 'sale_statistics.png')
    plt.savefig(chart_path)
    plt.close()
    
    return render(request, 'sale_list.html', {'sales': sales, 'chart_path': chart_path})


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

def main_info(request):
    cat_fact = get_cat_fact()
    return render(request, 'main_info.html', {'cat_fact': cat_fact})

def privacy_policy_page(request):
    random_gif_url = get_random_gif()
    return render(request, "gif.html", {"random_gif_url": random_gif_url})

def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            return redirect('product_reviews', product_id=product_id)
    else:
        form = ReviewForm()

    return render(request, 'product_reviews.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })