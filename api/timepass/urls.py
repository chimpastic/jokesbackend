from django.urls import path

from api.timepass import views

app_name = 'api.timepass'

urlpatterns = [
    path('jokes/', views.JokesView.as_view(), name='jokes'),
    #path('token/', views.CreateTokenView.as_view(), name='token'),
]
