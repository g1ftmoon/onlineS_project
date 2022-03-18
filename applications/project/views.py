from django.db.models import Q
from django.views.generic import ListView, DetailView

from applications.project.models import Product, Category, ProductImage


class ProductListView(ListView):
    paginate_by = 2
    model = Product
    template_name = 'home_page.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
        if category is not None:
            queryset = queryset.filter(category_id=category)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data()
        rating = 0
        carousel_images = ProductImage.objects.filter(product=self.kwargs['pk'])[1:]
        context['rating'] = rating
        context['carousel_images'] = carousel_images
        return context
