# myapp/urls.py
from rest_framework.routers import DefaultRouter
from .views import QueryViewSet

router = DefaultRouter()
router.register(r'queries', QueryViewSet)

urlpatterns = router.urls
