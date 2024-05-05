from django.contrib.auth.models import User
from django.db import models

from team.models import Team

class InfoTable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract =  True


class Comment(InfoTable):
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


class Client(InfoTable):
    ACTIVE = 'active'
    ARCHIVED = 'archived'

    CHOICES = (
        (ACTIVE, 'Active'),
        (ARCHIVED, 'Archived')
    )
    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comments = models.ManyToManyField(Comment, blank=True)
    status = models.CharField(max_length=255, choices=CHOICES, default=ACTIVE)


    class Meta:
        ordering = ['name',]
        verbose_name = 'Alyza Jimenez Blog'

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        print('Saved')
        super(Client, self).save(*args, *kwargs)
    
    def number_of_comments(self):
        return self.comments.count()


class TodoList(InfoTable):
    client = models.ForeignKey(Client, related_name='todolists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comments = models.ManyToManyField(Comment, blank=True)
    created_by = models.ForeignKey(User, related_name='todolists', on_delete=models.CASCADE)

