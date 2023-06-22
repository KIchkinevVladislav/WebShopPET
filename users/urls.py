from django.urls import path

from users.views import login, registrations, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registrations/', registrations, name='registrations'),
    path('profile/', profile, name='profile'),
]
