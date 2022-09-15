from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
	path('change-password/<user_token>/', views.change_password),
]
