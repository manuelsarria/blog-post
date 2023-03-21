from django.db import models

class Post  (models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField
  create_at = models.DateField(auto_created=True)
