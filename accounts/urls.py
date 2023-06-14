from django.urls import path
from . import views



urlpatterns = [
    path("signup/",views.userSignUp,name='sign_up'),
    path("login/",views.userLogin,name='login')
]