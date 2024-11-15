from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

UserModel = get_user_model()


class UserRegisterView(CreateView):
    pass


class UserLoginView(LoginView):
    pass


class ProfileEditView(UpdateView):
    pass


class ProfileDetailsView(DetailView):
    pass


class ProfileDeleteView(DeleteView):
    pass

