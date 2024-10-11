from django.urls import path 
from . import views

urlpatterns = [
    path('list/',views.list_view.as_view(),name= 'list'),
    path('<int:pk>/',views.BookDetailView.as_view(),name = 'detail'),
    path('create/',views.BookCreateView.as_view()),
    path('update/<int:pk>/',views.BookUpdateView.as_view()),
    path('delete/<int:pk>/',views.BookDeleteView.as_view()),
]
