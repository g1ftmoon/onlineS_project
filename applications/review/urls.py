from django.urls import path

from applications.review.views import AddReviewView, UpdateReviewView, DeleteReviewView

urlpatterns = [
    path('add-review/<int:pk>/', AddReviewView.as_view(), name='add-review'),
    path('update-review/<int:pk>', UpdateReviewView.as_view(), name='update-review'),
    path('delete-review/<int:pk>', DeleteReviewView.as_view(), name='delete-review'),
]
