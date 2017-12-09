from django.conf.urls import url
from .views import ReviewsListView, AddReviewView

urlpatterns = [
	url(r'^$', ReviewsListView.as_view(), name='reviews_list'),
	url(r'^add/$', AddReviewView.as_view(), name='add_review'),
]