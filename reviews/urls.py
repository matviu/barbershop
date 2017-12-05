from django.conf.urls import url
from .views import ReviewsListView

urlpatterns = [
	url(r'^$',ReviewsListView.as_view(), name='reviews_list')
]