from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .models import Review, ReviewPhoto
from .forms import AddReviewForm


class ReviewsListView(TemplateView):
	def get(self, request, *args, **kwargs):
		template_name = 'reviews/reviews_list.html'
		reviews = Review.objects.all()

		context = {
			'reviews': reviews,
		}

		return render(request, template_name, context)


class AddReviewView(FormView):
	form_class = AddReviewForm
	template_name = 'reviews/add_review.html'
	success_url = reverse_lazy('reviews_list', urlconf='reviews.urls')

	def post(self, request, *args, **kwargs):
		form = AddReviewForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			is_haircut = form.cleaned_data['is_haircut']
			is_shave = form.cleaned_data['is_shave']
			is_moustache = form.cleaned_data['is_moustache']

			review = Review.objects.create(name=name, description=description, is_haircut=is_haircut, is_shave=is_shave, is_moustache=is_moustache)

			review.save()

			for image in form.cleaned_data['images']:
				review_photo = ReviewPhoto.objects.create(image=image, review=review)
				review_photo.save()

			return HttpResponseRedirect(self.get_success_url())
		else:
			return render(request, self.template_name, {'form': form})



