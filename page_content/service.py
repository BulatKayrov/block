from .models import Block


def counter_views(slug):
    bloks = Block.objects.filter(page__slug=slug)
    for block in bloks:
        block.count_view += 1
        block.save()
