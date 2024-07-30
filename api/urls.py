from django.urls import path
from .views import CreateUserView, LoginView, LogoutView

urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]