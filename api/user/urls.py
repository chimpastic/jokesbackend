from django.urls import path

from api.user import views

app_name = 'api.user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManagedUserView.as_view(), name='me'),
]
