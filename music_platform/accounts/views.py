from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse

from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views


class SignUpView(CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('signup')
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse('artist-list')


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('artist-list')
