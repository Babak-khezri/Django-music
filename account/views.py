from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from music.models import Music
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login

# Create your views here.


class Home(LoginRequiredMixin, ListView):
    model = Music
    template_name = "registration/Home.html"


class UserCreateView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('account:home')

    def form_valid(self, form):
        valid = super(UserCreateView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
