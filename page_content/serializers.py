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


class BlockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Block
        exclude = ['page']


class PageSerializers(serializers.ModelSerializer):
    block = BlockSerializers(many=True)

    class Meta:
        model = Page
        fields = ['title', 'block']
