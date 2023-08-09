from rest_framework import serializers

from .models import Page, Block


class PagesSerializers(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ('title', 'link',)

    def get_link(self, obj):
        return 'http://127.0.0.1:8000' + obj.get_absolute_url()

    def get_title(self, obj):
        return obj.title_block()


class PageSerializers(serializers.ModelSerializer):
    block = serializers.SerializerMethodField()
    count_view_block = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ['title', 'count_view_block', 'block']

    def get_count_view_block(self, slug):
        queryset = Block.objects.filter(page__page__slug=slug)
        res = [
            {
                f'block_{item.title}': item.count_view
            }
            for item in queryset
        ]
        return res

    def get_block(self, slug):
        queryset = Block.objects.filter(page__page__slug=slug)
        res = [
            {
                'title': i.title,
                'link': i.link,
                'count_view': i.count_view,
                'sort': i.page.values('sort_index'),
            }
            for i in queryset
        ]
        return res
