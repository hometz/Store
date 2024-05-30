from django import forms
from .models import Product, Customer, Sale, SaleProduct, CustomerAddress
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'

class SaleProductForm(forms.ModelForm):
    class Meta:
        model = SaleProduct
        fields = '__all__'

class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerAddress
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
