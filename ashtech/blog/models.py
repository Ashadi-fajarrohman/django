from django.db import models
from users.models import Users


# Create your models here.
class Comment(models.Model):
    text_comment = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ForeignKey('Photos', on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)


class Photos(models.Model):
    caption = models.TextField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    memes_photo = models.ImageField()
    upload = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.upload}"
