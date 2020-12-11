from django.db import models
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse # for django 1.9
from django.urls import reverse     # for django 3

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=512)
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    objects = QuestionManager()

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('single-question', kwargs={'question_id': self.pk})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.text