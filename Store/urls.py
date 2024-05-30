"""
URL configuration for Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from Store import settings
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('latest/', views.latest_article, name='latest_article'),
    path('about/', views.about_us, name='about_us'),
    path('news/', views.article_list, name='article_list'),
    path('news/<int:pk>/', views.article_detail, name='article_detail'),
    path('faq/', views.faq_list, name='faq_list'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('panel/', views.admin_page, name='admin_page'),

    path('product/create/', views.create_product, name='create_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/update/', views.update_product, name='update_product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('product/list/', views.product_list, name='product_list'),

    # URL-шаблоны для клиентов
    path('customer/create/', views.create_customer, name='create_customer'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customer/<int:pk>/update/', views.update_customer, name='update_customer'),
    path('customer/<int:pk>/delete/', views.delete_customer, name='delete_customer'),
    path('customer/list/', views.customer_list, name='customer_list'),

    # URL-шаблоны для продаж
    path('sale/create/', views.create_sale, name='create_sale'),
    path('sale/<int:pk>/', views.sale_detail, name='sale_detail'),
    path('sale/<int:pk>/update/', views.update_sale, name='update_sale'),
    path('sale/<int:pk>/delete/', views.delete_sale, name='delete_sale'),
    path('sale/list/', views.sale_list, name='sale_list'),
    path('saleproduct/create/', views.create_sale_product, name='create_sale_product'),
    path('customeraddress/create/', views.create_customer_address, name='create_customer_address'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
