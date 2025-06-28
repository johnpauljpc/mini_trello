from django.db import models
from datetime import datetime, timedelta
from boards.models import Board


next_3_days = (datetime.now() + timedelta(days=3)).date()
# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('in-progress', 'In Progress'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateField(blank=True, null=True, default=next_3_days)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['board', 'status', '-date_created'] # Order tasks by board, then status, then creation date

    def __str__(self):
        return f"{self.title} (Board: {self.board.board_name}, Status: {self.status})"