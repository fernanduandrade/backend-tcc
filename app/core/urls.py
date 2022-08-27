from rest_framework import routers
from .views import PlaceViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('place', PlaceViewSet, basename='place')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = router.urls