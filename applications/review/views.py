from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import UpdateView

from applications.project.models import Product
from applications.review.forms import AddReviewForm, UpdateReviewForm
from applications.review.models import Review


class AddReviewView(LoginRequiredMixin, View):

    def post(self, request, pk):
        form = AddReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            product = Product.objects.get(id=pk)
            form.product = product
            form.author_id = request.user.id
            form.save()
        return redirect(product.get_absolute_url())


class UpdateReviewView(LoginRequiredMixin, UpdateView):
    model = Review
    template_name = 'update_review.html'
    form_class = UpdateReviewForm
    context_object_name = 'review'


class DeleteReviewView(View):

    def get(self, request, pk):
        review = Review.objects.get(id=pk)
        review.delete()
        return redirect(review.get_absolute_url())