from django.conf.urls import url
from django.views.generic import TemplateView
from .views import PhotosListView

urlpatterns = [
	url(r'^$', PhotosListView.as_view(), name='photos_list')
]