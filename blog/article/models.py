from django.db import models

# Create your models here.

class Article(models.Model):

    author = models.ForeignKey("auth.User", on_delete = models.CASCADE,verbose_name = "Author")
    title = models.CharField(max_length = 50, verbose_name = "Title")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = "Date Created")

    def __str__(self):
        return self.title

