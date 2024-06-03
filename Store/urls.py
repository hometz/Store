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
    path('products/', views.product_list, name='products_list'),
    path('products/edit/<int:pk>', views.edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('products/create/', views.create_product, name='create_product'),
    path('buy_product/<int:product_id>/', views.buy_product, name='buy_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
