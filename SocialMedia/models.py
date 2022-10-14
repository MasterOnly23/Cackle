
from time import timezone
import django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares' ,default="default.png", blank=True)


    def __str__(self) -> str:
        return f'Perfil de {self.user.username}'


    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user).values_list('to_user_id', flat=True)

        return User.objects.filter(id__in=user_ids)

    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user).values_list('from_user_id', flat=True)

        return User.objects.filter(id__in=user_ids)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp'] #ordenar en orden asc
        
    def __str__(self) -> str:
        return f'{self.user.username}:{self.content}'


class Relationship(models.Model): #relcion entre los usuarios
    from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.from_user} to {self.to_user}'

    class Meta:
        indexes = [
            models.Index(fields=['from_user', 'to_user',]),
        ]


class Country(models.Model):

    COUNTRY_CHOICES = (
    ('', '-----'),
    ('Argentina', 'Argentina'),
    ('Belice', 'Belice'),
    ('Bolivia', 'Bolivia'),
    ('Brasil', 'Brasil'),
    ('Canada', 'Canada'),
    ('Chile', 'Chile'),
    ('Colombia', 'Colombia'),
    ('Costa Rica', 'Costa Rica'),
    ('Cuba', 'Cuba'),
    ('Curazao', 'Curazao'),
    ('Aruba', 'Aruba'),
    ('Ecuador', 'Ecuador' ),
    ('El Salvador', 'El Salvador'),
    ('Guatemala', 'Guatemala'),
    ('Haiti', 'Haiti'),
    ('Honduras', 'Honduras'),
    ('Jamaica', 'Jamaica'),
    ('Mexico', 'Mexico'),
    ('Nicaragua', 'Nicaragua'),
    ('Panama', 'Panama'),
    ('Paraguay', 'Paraguay'),
    ('Peru', 'Peru'),
    ('Puerto Rico', 'Puerto Rico'),
    ('Republica Dominicana', 'Republica Dominicana'),
    ('United States', 'United States'),
    ('Uruguay', 'Uruguay'),
    ('Venezuela', 'Venezuela'),
)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30, choices=COUNTRY_CHOICES)

    def __str__(self) -> str:
        return f'{self.country}'