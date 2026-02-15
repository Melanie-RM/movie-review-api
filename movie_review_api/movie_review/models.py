from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#movie model
class Movie(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


#review model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'reviews')
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE, related_name = 'reviews')
    rating = models.IntegerField() # 1 - 5 star ratings
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = ('user','movie')  #one user per movie

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
    


#like model 
class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.ForeignKey (Review, on_delete = models.CASCADE, related_name = 'Likes')
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('user', 'review')
    
    def __str__(self):
        return f"{self.user.username} likes {self.review}"

#genre model 
class Genre(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name
