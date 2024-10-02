from django.urls import path
from .views import login_view, create_account_view, logout_view, UserListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', login_view, name='login'),
    path('create-account/', create_account_view, name='create-account'),
    path('user-list/', UserListView.as_view(), name='user-list'),
    path('edit-user/<int:pk>/', UserUpdateView.as_view(), name='edit-user'),
    path('user-confirm-delete/<int:pk>/', UserDeleteView.as_view(), name='user-confirm-delete'),
    path('logout/', logout_view, name='logout')
]
