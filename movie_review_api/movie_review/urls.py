from rest_framework.routers import DefaultRouter
from . import views
from .views import MovieViewSet, ReviewViewSet, LikeViewSet
from django.urls import path, include
from .views import tmdb_search, tmdb_popular
from django.contrib import admin

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movie_review.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('profile',views.profile, name = 'profile')
]