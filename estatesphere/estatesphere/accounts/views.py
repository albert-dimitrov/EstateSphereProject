from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth import login, logout
from estatesphere.accounts.models import Profile, CustomUser

from estatesphere.accounts.forms import AppUserCreationForm, ProfileEditForm
from estatesphere.properties.models import RealEstateProperty

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


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['properties_count'] = self.object.estate_properties.count()

        total_rating = 0
        total_estates = 0
        for real_estate in self.object.estate_properties.all():
            total_estates += 1
            current_reviews = 0
            current_rating = 0
            for r in real_estate.reviews.all():
                current_rating += r.rating
                current_reviews += 1

            if current_reviews:
                total_rating += current_rating // current_reviews
            else:
                total_estates -= 1

        avg_rating = total_rating // total_estates if total_rating else None

        context['avg_rating'] = avg_rating if avg_rating else None

        return context


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('login')

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def form_valid(self, form):

        user = CustomUser.objects.get(pk=self.object.pk)
        user.is_active = False
        user.save()

        logout(self.request)

        response = super().form_valid(form)

        return response


class ProfilePropertiesView(LoginRequiredMixin, ListView):
    model = RealEstateProperty
    template_name = 'accounts/profile-my-properties.html'
    context_object_name = 'all_properties'

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(user__pk=self.request.user.pk)

        return queryset


class MyFavouriteProperties(LoginRequiredMixin, ListView):
    model = RealEstateProperty
    template_name = 'accounts/profile-favourite-properties.html'
    context_object_name = 'all_properties'

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(favourites__user=self.request.user)

        return queryset

