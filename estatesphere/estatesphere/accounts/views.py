from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth import login, logout
from estatesphere.accounts.models import Profile, CustomUser

from estatesphere.accounts.forms import AppUserCreationForm, ProfileEditForm

UserModel = get_user_model()


class UserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class UserLoginView(LoginView):
    template_name = 'accounts/login-page.html'


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileDetailsView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['properties_count'] = self.object.estate_properties.count()

        total_rating = 0
        total_estates = 0
        for real_estate in self.object.estate_properties.all():
            total_estates += 1
            total_rating += sum([r.rating for r in real_estate.reviews.all()])

        avg_rating = total_rating // total_estates if total_rating else None

        context['avg_rating'] = avg_rating if avg_rating else None

        return context


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        user = CustomUser.objects.get(pk=self.object.pk)
        user.is_active = False
        user.save()

        logout(self.request)

        response = super().form_valid(form)

        return response


