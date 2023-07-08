from django.urls import path

from users.views import login, UserRegistrarionView, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registrations/', UserRegistrarionView.as_view(), name='registrations'),
    path('profile/', profile, name='profile'),
]
