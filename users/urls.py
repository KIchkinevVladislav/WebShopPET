from django.urls import path

from users.views import login, registrations, profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registrations/', registrations, name='registrations'),
    path('profile/', profile, name='profile'),
]
