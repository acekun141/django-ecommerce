from django import forms
from django.contrib.auth.models import User
from customers.models import Customer


class CustomerForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)

    def clean_password2(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            msg = 'Password not correct!'
            raise forms.ValidationError(msg)
        if 30 < len(password1) < 6:
            msg = 'Password to short'
            raise forms.ValidationError(msg)

        return password2
    
    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        user_with_same_email = User.objects.filter(email=email)
        if user_with_same_email:
            msg = 'Email existed!'
            raise forms.ValidationError(msg)

        return email

class CustomerInfoForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ['avatar', 'first_name', 'last_name', 'phonenumber', 'address']