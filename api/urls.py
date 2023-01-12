from django.urls import path, include


urlpatterns = [
    path('user/', include('api.user.urls')),
    path('product/', include('api.product.urls')),
    path('timepass/', include('api.timepass.urls'))

]
