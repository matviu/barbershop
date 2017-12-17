from django.conf.urls import url
from .views import EntryView

urlpatterns = [
	url(r'^$', EntryView.as_view(), name='entry_form')
]
