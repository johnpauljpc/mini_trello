from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify



USER = get_user_model()
# Create your models here.

VISIBILITY_CHOICES = (('public', 'Public'),
                      ('private', 'Private'))

class Board(models.Model):
    board_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    visibility = models.CharField(choices=VISIBILITY_CHOICES, max_length=100)
    owner = models.ForeignKey(USER, on_delete=models.CASCADE, related_name="boards")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        # Ensures that a user cannot have two boards with the exact same name
        unique_together = ('board_name', 'owner')
        ordering = ['-date_created']

    @property
    def tasks_count(self):
        return 2
    
    def __str__(self):
        return self.board_name
    
    # To make make board name slugified os that it can be used as the lookup keyword
    def save(self, *args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.board_name)
            slug = base_slug
            num = 1

            while Board.objects.filter(slug = slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug

        self.full_clean() #To ensure clean method is always called.
        super().save(*args, **kwargs)

