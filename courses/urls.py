from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,  CourseViewSet

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = router.urls
