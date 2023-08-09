from .models import Block, PageBlock, Page


def counter_views(slug):
    data = Block.objects.filter(page__page__slug=slug)
    for i in data:
        i.count_view += 1
        i.save()

