from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Movie, Review, Like
from .serializers import MovieSerializer, ReviewSerializer, LikeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from collections import Counter
from rest_framework.decorators import api_view
from .tmdb import search_movies, get_popular_movies

# Create your views here.

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    def recommendations(self,request):
        user = request.user
        user_reviews = Review.objects.filter(user = user, rating__gte = 4)

        if not user_reviews.exists():
            return Response({"message": "No recommendations available. Please review movies first!"})
        

        genres = [review.movie.genre for review in user_reviews]
        genre_counts = Counter(genres)
        favorite_genres = [genre for genre, count in genre_counts.items()]
        reviewed_movie_ids = user_reviews.values_list('movie_id', flat = True)
        recommended_movies = Movie.objects.filter(genre__in = favorite_genres).exclude(id__in = reviewed_movie_ids).distinct()
        serializer = MovieSerializer(recommended_movies, many = True)
        return Response(serializer.data)
       
    


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class LikeViewSet (viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def  perform_create(self, serializer):
        serializer.save(user = self.request.user
                        )
@api_view(['GET'])       
def tmdb_search(request):
    query = request.GET.get('query')
    if not query:
        return Response({"error":"Query parameter is required"})
    data = search_movie(query)
    return Response(data)

@api_view(['GET'])
def tmdb_popular(request):
    data = get_popular_movies()
    return Response(data)