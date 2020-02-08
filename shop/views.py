from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import View
from shop.models import Product


class HomePageView(View):
    template_name = 'shop/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

class ShopView(View):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    def get(self, request):
        try:
            products = self.model.objects.all()
        except:
            return Http404
        return render(request, template_name=self.template_name,
                      context={self.context_object_name: products})

class ProductView(View):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'product'

    def query_set(self, pk):
        query = get_object_or_404(self.model, pk=pk)
        return query

    def get(self, request, pk, *args, **kwargs):
        return render(request, template_name=self.template_name,
                      context={self.context_object_name: self.query_set(pk=pk)})