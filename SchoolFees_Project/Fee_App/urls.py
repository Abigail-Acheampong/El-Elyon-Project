from django.urls import path
from .import views
from .views import FeeListCreateView, FeeRetrieveUpdateDestroyView

urlpatterns = [
    path('fees/', views.fee_list, name='fee_list'),
    path('fees/add/', views.add_fee, name='add_fee'),
    path('fees/edit/<int:pk>/', views.edit_fee, name='edit_fee'),
    path('fees/delete/<int:pk>/', views.delete_fee, name='delete_fee'),
    
    path('fees/', FeeListCreateView.as_view(), name='fee-list-create'),
    path('fees/<int:pk>/', FeeRetrieveUpdateDestroyView.as_view(), name='fee-detail'),
]
