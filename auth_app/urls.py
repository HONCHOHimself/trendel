from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.register_view),
]