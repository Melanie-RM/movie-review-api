from django.contrib import admin
from .models import Movie, Review, Like

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','release_date','created_at')
    search_fields = ('title',)
    list_filter = ('release_date',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'created_at')
    search_fields = ('user_username', 'movie_title')
    list_filter = ('rating',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'review', 'created_at')