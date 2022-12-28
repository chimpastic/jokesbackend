from django.urls import path, include
from rest_framework.routers import DefaultRouter


from api.product import views

router = DefaultRouter()
router.register('cat', views.CategoryViewSet)
router.register('product', views.ProductViewSet)

appname = 'product'

urlpatterns = [path('', include(router.urls))]
