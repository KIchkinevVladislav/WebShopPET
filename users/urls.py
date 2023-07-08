from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import UserLoginView, UserRegistrarionView, UserProfileView, logout

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('registrations/', UserRegistrarionView.as_view(), name='registrations'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
]
