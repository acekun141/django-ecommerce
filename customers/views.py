from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import View
from customers.forms import CustomerForm, CustomerInfoForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from customers.models import Customer

class CustomerView(LoginRequiredMixin, View):
    login_url = '/customer/signin/'
    redirect_field_name = None
    template_name = 'customers/profile.html'
    context_user_name = 'user'
    context_customer_name = 'customer'

    def get_user(self, email):
        user = get_object_or_404(User, username=email)
        return user

    def get(self, request):
        user = self.get_user(request.user)
        customer = user.customer_set.first()
        return render(request, template_name=self.template_name,
                      context={self.context_user_name: user,
                               self.context_customer_name: customer})


class CustomerInfoView(LoginRequiredMixin, View):
    template_name = 'customers/form_profile.html'

    def get(self, request):
        form = CustomerInfoForm()
        print(form)
        return render(request, template_name=self.template_name,
                      context={'form': form})


class SignUpView(View):
    form = CustomerForm()
    template_name = 'customers/signup.html'
    context_object_name = 'form'

    def get(self, request):
        return render(request, template_name=self.template_name,
                      context={self.context_object_name: self.form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            new_user = User.objects.create_user(email=email, username=email, password=password)
            new_user.save()
            return HttpResponseRedirect(reverse(viewname='signup'))
        else:
            return render(request, template_name=self.template_name,
                          context={self.context_object_name: form})
        

class SignInView(View):
    template_name = 'customers/signin.html'
    
    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        try:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if not user:
                raise Exception
        except Exception as value:
            return render(request, template_name=self.template_name,
                          context={'errors': 'Email or Password not correct!'})
        
        login(request, user)
        return HttpResponseRedirect(reverse(viewname='shop'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse(viewname='homepage'))