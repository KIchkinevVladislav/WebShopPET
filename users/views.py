
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('index')

# def login(request):
#     if request.method == 'POST':
#         form=UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)  
#                 return HttpResponseRedirect(reverse('index'))             
#     else:
#         form = UserLoginForm
#     context = {'form': form}
#     return render(request, 'users/login.html', context)


class UserRegistrarionView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Store - Регистрация'
        return context

# def registrations(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Поздравляем. Вы успешно зарегистрированы!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    
    # переопредялем метод для для получения текущего пользователя
    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({'title': 'Store - Личный кабинет',
                        'baskets': Basket.objects.filter(user=self.object)})
        return context
    
    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#            print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)

#     context = {
#         'title': 'Store - Профиль', 
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user),
#         }
#     return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))