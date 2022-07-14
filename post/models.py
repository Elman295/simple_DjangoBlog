from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(to="auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title






