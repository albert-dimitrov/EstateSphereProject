from django.contrib.auth.views import LogoutView
from django.urls import path, include
from estatesphere.accounts import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('details/', views.ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
        path('my-properties/', views.ProfilePropertiesView.as_view(), name='profile-properties'),
        path('favourites/', views.MyFavouriteProperties.as_view(), name='my-favourite')
    ]))
]