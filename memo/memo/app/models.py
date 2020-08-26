from django.db import models

# Create your models here.
class Memo(models.Model):
    
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    deleted_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'メモ'
        ordering = ['-created_datetime']
        
    def __str__(self):
        return self.title
