from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    sort_page = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('page_content:block', args=[self.slug])

    def title_block(self):
        block_titles = self.block.values_list('title', flat=True)
        return list(block_titles)

    def __str__(self):
        return f'{self.title}'


class Block(models.Model):
    title = models.CharField(max_length=50)
    link = models.TextField()
    sort_block = models.IntegerField(default=0)
    count_view = models.IntegerField(default=0)
    page = models.ManyToManyField(Page, related_name='block')

    def __str__(self):
        return f'{self.title}'
