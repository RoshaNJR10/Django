from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.function, name='home'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('email/',views.email, name='email'),

]
