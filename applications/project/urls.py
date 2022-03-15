from django.urls import path

from applications.project.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home-page'),
]
