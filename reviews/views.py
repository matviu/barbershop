from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse
from .models import Review
from .forms import AddReviewForm


class ReviewsListView(TemplateView):

	def get(self, request):
		template_name = 'reviews/reviews_list.html'
		reviews = Review.objects.all()

		context = {
			'reviews': reviews,
		}

		return render(request, template_name, context)


class AddReviewView(FormView):
	form_class = AddReviewForm
	template_name = 'reviews/add_review.html'
	success_url = '/reviews/'

	def post(self, request):
		form = AddReviewForm(request.POST, request.FILES)
		if form.is_valid():
			print('*************form.cleaned_data', form.cleaned_data)
			return HttpResponseRedirect(self.get_success_url())
		else:
			print('*************form NOT VALID')
			return HttpResponseRedirect('/reviews/')




