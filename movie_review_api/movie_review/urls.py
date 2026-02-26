from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = router.urls