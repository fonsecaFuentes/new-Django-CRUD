from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    completed = models.DateTimeField(null=True, blank=True)
    image1 = models.ImageField(
        default='img_task1.png',
        upload_to='img_tasks/',
        verbose_name='Imagen',
        blank=True
    )
    image2 = models.ImageField(
        default='img_task2.png',
        upload_to='img_tasks/',
        verbose_name='Imagen',
        blank=True
    )

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f"Tarea - {self.title} - Creada por: {self.user}"

    @property
    def creator_username(self):
        return self.user.username
