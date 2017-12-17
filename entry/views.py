from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EntryForm


class EntryView(TemplateView):
	template_name = 'entry/entry.html'


	def get(self, request, *args, **kwargs):
		form = EntryForm()

		return render(request, self.template_name, {'form': form })
