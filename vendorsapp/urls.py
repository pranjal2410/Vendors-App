from django.urls import path

from .views import SignupView, HomeView, VendorView, LoginView, MainView, DetailsView, SearchView, LogoutView, \
    ProfileView, VendorUpdate, VendorDelete, ProfileDelete, Search

urlpatterns = [
    path('home/ajax/search/', Search.as_view(), name='searching'),
    path('', MainView.as_view(), name='main'),
    path('Signup/', SignupView.as_view(), name='Signup'),
    path('login/', LoginView.as_view(), name='Login'),
    path('Create/', VendorView.as_view(), name='Create'),
    path('home/', HomeView.as_view(), name='home'),
    path('details/<int:pk>/', DetailsView.as_view(), name='details'),
    path('search/', SearchView.as_view(), name='search'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update/<int:pk>/', VendorUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', VendorDelete.as_view(), name='delete'),
    path('delete_profile/<int:pk>/', ProfileDelete.as_view(), name='deactivateProfile')
]
