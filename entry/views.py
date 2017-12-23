from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from .forms import EntryForm


class EntryView(FormView):
	template_name = 'entry/entry.html'

	def get(self, request, *args, **kwargs):
		form = EntryForm()
		return render(request, self.template_name, {'form': form })

	def post(self, request, *args, **kwargs):
		form = EntryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, self.template_name, {'form': form })