from django import forms
from .models import Product, Customer, Sale, SaleProduct, CustomerAddress, Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ProductEdit(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    unit = forms.ChoiceField(choices=Product.UNIT_CHOICES)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating']

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 0:
            raise forms.ValidationError("Рейтинг не может быть меньше 0.")
        elif rating > 10:
            raise forms.ValidationError("Рейтинг не может быть больше 10.")
        return rating

class SaleProductForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    quantity = forms.IntegerField(min_value=1)
    promo_code = forms.CharField(max_length=20, required=False)

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
