from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import login, UserRegistrarionView, UserProfileView, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registrations/', UserRegistrarionView.as_view(), name='registrations'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
]
