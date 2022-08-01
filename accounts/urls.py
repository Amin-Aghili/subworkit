from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', views.UserProfileEditView.as_view(), name='profile_edit'),
]
