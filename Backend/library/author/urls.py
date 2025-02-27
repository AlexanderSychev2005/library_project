from django.urls import path
from .views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView

urlpatterns = [
    path('', AuthorListView.as_view(), name='author_list'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('create/', AuthorCreateView.as_view(), name='author_create'),
    path('<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),

]