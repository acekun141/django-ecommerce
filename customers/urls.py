from django.urls import path
from customers.views import (
        SignUpView, SignInView,
        logout_user, CustomerView,
        CustomerInfoView)

urlpatterns = [
    path('', CustomerView.as_view(), name='customer-profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', logout_user, name='logout'),
    path('edit/', CustomerInfoView.as_view(), name='edit'),
]