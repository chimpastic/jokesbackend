from django.urls import path, include
from rest_framework.routers import DefaultRouter


from api.product import views

router = DefaultRouter()
router.register('cat', views.CategoryViewSet)

appname = 'product'

urlpatterns = [path('', include(router.urls))]
