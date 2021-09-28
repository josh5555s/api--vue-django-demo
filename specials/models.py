from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Special(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500, default='')
    locations = models.CharField(max_length=50)
    reoccuring_weekend = models.CharField(max_length=50, blank=True)
    start_date = models.CharField(max_length=50, default='')
    start_time = models.FloatField(max_length=50, default=0.0)
    end_date = models.CharField(max_length=50, default='')
    end_time = models.FloatField(max_length=50, default=0.0)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title