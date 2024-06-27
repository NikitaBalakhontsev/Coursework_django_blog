from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.resources, name='resources'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail')
]
