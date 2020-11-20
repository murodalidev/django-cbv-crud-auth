from django.urls import path
from app.views import *
from django.views.generic import TemplateView
# from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', TemplateView.as_view(template_name='app/home.html'), name='home'),

    path('auth/register/', UserRegisterView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('auth/logout/', UserLogoutView.as_view(), name='logout'),
    # path('auth/logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('account/update/<int:pk>', UserUpdateView.as_view(), name='account'),

    path('publishers/', PublisherListView.as_view(), name='publisher'),
    path('publisher/<int:pk>/', PublisherDetailView.as_view(), name='publisher-detail'),
    path('publisher/create/', PublisherCreateView.as_view(), name='publisher-create'),
    path('publisher/<int:pk>/update/', PublisherUpdateView.as_view(), name='publisher-update'),
    path('publisher/<int:pk>/delete/', PublisherDeleteView.as_view(), name='publisher-delete'),

    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', AuthorCreateView.as_view(), name='author-create'),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),

    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/create/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

]
