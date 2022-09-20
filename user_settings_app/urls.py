from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
	path('get-user/<user_token>/', views.get_user),
	
	path('change-password/<user_token>/', views.change_password),
		# current_password
		# new_password
]
