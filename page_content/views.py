from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Page
from .serializers import PagesSerializers, PageSerializers
from .service import counter_views


class PagesView(APIView):

    def get(self, request, slug=None):
        if slug:
            counter_views(slug=slug)
            queryset = Page.objects.get(slug=slug)
            serializer = PageSerializers(queryset)
            return Response({'result': serializer.data})
        else:
            queryset = Page.objects.all()
            serializer = PagesSerializers(queryset, many=True)
            return Response({'result': serializer.data})

