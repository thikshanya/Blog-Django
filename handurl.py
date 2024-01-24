from rest_framework.routers import DefaultRouter 
from .views import BlogViewSet

router = DefaultRouter()
router.register('',BlogViewSet)

urlpatterns = [
    path('',include(router.urls)),
]