from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, EmployerDetailView, UserChangeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>', EmployerDetailView.as_view(template_name='employer_profile.html'),
         name='employer_profile'),
    path('change_profile/<int:pk>', UserChangeView.as_view(), name='user_update'),

]
