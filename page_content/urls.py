from django.urls import path

from .views import PagesView

app_name = 'page_content'

urlpatterns = [
    path('pages/', PagesView.as_view(), name='pages'),
    path('page/<slug:slug>/', PagesView.as_view(), name='block'),
]
