from django.db import models
from django.contrib.auth.models import User



class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.FloatField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.subject}: {self.score}"
